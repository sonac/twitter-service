from . import client
from app import app
import responses


@responses.activate
def fetch(client, user):
    return client.post('/fetch', data=dict(
        user=user
    ))


def avg_length(client):
    return client.get('/avg-length')


def user_avg_length(client, user):
    return client.get('/avg-length/' + user)


def coolest_follower(client, user):
    return client.get('/coolest-follower/' + user)


def test_index(client):
    rv = client.get('/')
    assert b'Welcome to Twitter Service' in rv.data


def test_fetch(client):
    rv = fetch(client, 'test_screen_name')
    assert b'I am not real' in rv.data


def test_non_existing_user(client):
    rv = fetch(client, 'non_existing_user')
    assert '400 BAD REQUEST' == rv.status


def test_avg_length(client):
    rv = avg_length(client)
    assert b'13.0' in rv.data


def test_user_avg_length(client):
    rv = user_avg_length(client, 'test_screen_name')
    assert b'13.0' in rv.data


def test_coolest_follower(client):
    rv = coolest_follower(client, 'test_screen_name')
    assert b'test_screen_name3' in rv.data
