from datetime import datetime
import unittest
from app import app, db
from app.models import User, Tweet, UserFollower


class UserModelTest(unittest.TestCase):
    def setUp(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_get_user_tweets_empty(self):
        u = User()
        assert(u.get_user_tweets() == [])

    def test_get_user_tweets(self):
        u = User(id=123, name='test', screen_name='test_screen_name', location='nowhere',
                 url='localhost', description='test_description', followers_count=0)
        db.session.add(u)
        db.session.add(Tweet(id_str='456', created_at=datetime.now(),
                             text='Some random text', user_id=123))
        db.session.commit()
        assert(str(u.get_user_tweets()[0]) == 'Some random text')

    def test_get_avg_tweet_length(self):
        u = User(id=123, name='test', screen_name='test_screen_name', location='nowhere',
                 url='localhost', description='test_description', followers_count=0)
        db.session.add(u)
        db.session.add(Tweet(id_str='456', created_at=datetime.now(),
                             text='Some random text', user_id=123))
        db.session.commit()
        assert(u.get_avg_tweet_length() == 16.0)

    def test_get_coolest_follower(self):
        u = User(id=123, name='test', screen_name='test_screen_name', location='nowhere',
                 url='localhost', description='test_description', followers_count=2)
        f1 = User(id=124, name='test', screen_name='test_follower1', location='nowhere',
                  url='localhost', description='test_description', followers_count=0)
        f2 = User(id=125, name='test', screen_name='test_follower2', location='nowhere',
                  url='localhost', description='test_description', followers_count=1)
        db.session.add(u)
        db.session.add(f1)
        db.session.add(f2)
        db.session.add(UserFollower(user_id=123, follower_id=124))
        db.session.add(UserFollower(user_id=123, follower_id=125))
        db.session.commit()
        assert('test_follower2' in str(u.get_coolest_follower()))
