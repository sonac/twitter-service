from tweepy import Cursor
from sqlalchemy.sql import func
from config import TwitterConfig
from app.models import Tweet, User, Hashtag, UserFollower
from app import db


class TwitterService(TwitterConfig):
    def __init__(self, tweepy):
        auth = tweepy.OAuthHandler(self.CONSUMER_KEY, self.CONSUMER_SECRET)
        auth.set_access_token(self.ACCESS_TOKEN, self.ACCESS_TOKEN_SECRET)
        self.api = tweepy.API(auth)

    # using merge in all sqlalchemy methods to avoid PK voilation in case of duplicate calls
    def fetch_user_tweets(self, username, count):
        twitter_user = self.api.get_user(username)
        # adding user to db
        user = User(id=twitter_user.id, name=twitter_user.name, screen_name=twitter_user.screen_name, location=twitter_user.location,
                    url=twitter_user.url, description=twitter_user.description, followers_count=twitter_user.followers_count)
        db.session.merge(user)
        for follower in twitter_user.followers():
            # adding each follower as user to db and then establishing links user -> follower
            db.session.merge(User(id=follower.id, name=follower.name, screen_name=follower.screen_name, location=follower.location,
                                  url=follower.url, description=follower.description, followers_count=follower.followers_count))
            db.session.merge(UserFollower(
                user_id=twitter_user.id, follower_id=follower.id))
        db.session.commit()
        user = db.session.query(User).filter(func.lower(
            User.screen_name) == func.lower(twitter_user.screen_name)).first()
        for tweet in Cursor(self.api.user_timeline, id=username).items(count):
            # adding each tweet from cursor
            db.session.merge(Tweet(id_str=tweet.id_str, created_at=tweet.created_at,
                                   text=tweet.text, user_id=tweet.user.id))
            for hashtag in tweet.entities['hashtags']:
                # and hashtags for it with links to proper tweets
                db.session.merge(Hashtag(
                    text=hashtag['text'], indices=' '.join(str(ind) for ind in hashtag['indices']), tweet_id=tweet.id_str))
        db.session.commit()
        return '\n'.join([str(tweet) for tweet in user.get_user_tweets()])

    def get_average_tweet_length(self, user):
        if (user is None):
            return str(round(db.session.query(func.avg(func.length(Tweet.text))).scalar(), 2))
        else:
            user = db.session.query(User).filter(
                func.lower(User.screen_name) == func.lower(user)).scalar()
            return str(round(user.get_avg_tweet_length(), 2))

    def coolest_follower(self, user):
        user = db.session.query(User).filter(
            func.lower(User.screen_name) == func.lower(user)).scalar()
        return str(user.get_coolest_follower())
