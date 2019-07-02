from sqlalchemy.sql import func

from app import db


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.BigInteger, primary_key=True)
    name = db.Column(db.Text)
    screen_name = db.Column(db.Text)
    location = db.Column(db.Text)
    url = db.Column(db.Text)
    description = db.Column(db.Text)
    followers_count = db.Column(db.Integer)

    def __repr__(self):
        return f'User {self.screen_name} with {self.followers_count} followers'

    def get_user_tweets(self):
        return db.session.query(Tweet).filter(Tweet.user_id == self.id).all()

    def get_avg_tweet_length(self):
        return db.session.query(func.avg(func.length((Tweet.text)))).filter(Tweet.user_id == self.id).scalar()

    def get_coolest_follower(self):
        return db.session.query(User)\
            .filter(UserFollower.follower_id == User.id, UserFollower.user_id == self.id)\
            .order_by(User.followers_count.desc()).first()


class Tweet(db.Model):
    __tablename__ = "tweets"
    id_str = db.Column(db.Text, primary_key=True)
    created_at = db.Column(db.DateTime)
    text = db.Column(db.Text)
    user_id = db.Column(db.BigInteger, db.ForeignKey('users.id'))

    def __repr__(self):
        return self.text


class UserFollower(db.Model):
    __tablename__ = "user_followers"
    user_id = db.Column(db.BigInteger, db.ForeignKey(
        'users.id'), primary_key=True)
    follower_id = db.Column(db.BigInteger, db.ForeignKey(
        'users.id'), primary_key=True)


class Hashtag(db.Model):
    __tablename__ = "hashtags"
    text = db.Column(db.Text, primary_key=True)
    indices = db.Column(db.Text)
    tweet_id = db.Column(db.Text, db.ForeignKey(
        'tweets.id_str'), primary_key=True)
