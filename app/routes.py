from flask import abort, request

from app import app
from app.services import TwitterService

import tweepy

twitter_service = TwitterService(tweepy)


@app.route('/')
def index():
    return 'Welcome to Twitter Service'


@app.route('/fetch', methods=['POST'])
def fetch():
    try:
        user = request.form['user']
        return twitter_service.fetch_user_tweets(user, 5)
    except tweepy.TweepError as e:
        print(e)
        return abort(400)


@app.route('/avg-length')
@app.route('/avg-length/<user>')
def avg_length(user=None):
    return twitter_service.get_average_tweet_length(user)


@app.route('/coolest-follower/<user>')
def coolest_follower(user):
    try:
        return twitter_service.coolest_follower(user)
    except:
        return abort(400)
