import os
import tempfile

import pytest
import responses
import json

from app import app, db


@pytest.fixture
def client():
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(
        tempfile.gettempdir(), 'test.db')
    with app.app_context():
        db.create_all()
    app.config['TESTING'] = True
    # Mocking response for user object
    responses.add(responses.GET,
                  'https://api.twitter.com/1.1/users/show.json?id=test_screen_name',
                  json={
                      "id": 123,
                      "name": "test",
                      "screen_name": "test_screen_name",
                      "location": "nowhere",
                      "url": "localhost",
                      "description": "mocked_test_user",
                      "followers_count": 2
                  }, status=200)
    # Mocking response for followers
    responses.add(responses.GET,
                  'https://api.twitter.com/1.1/followers/list.json?user_id=123',
                  json={
                      "users": [
                          {
                              "id": 111,
                              "name": "test1",
                              "screen_name": "test_screen_name1",
                              "location": "nowhere",
                              "url": "localhost",
                              "description": "mocked_test_user",
                              "followers_count": 1
                          },
                          {
                              "id": 222,
                              "name": "test2",
                              "screen_name": "test_screen_name2",
                              "location": "nowhere",
                              "url": "localhost",
                              "description": "mocked_test_user",
                              "followers_count": 2
                          },
                          {
                              "id": 333,
                              "name": "test3",
                              "screen_name": "test_screen_name3",
                              "location": "nowhere",
                              "url": "localhost",
                              "description": "mocked_test_user",
                              "followers_count": 3
                          }
                      ],
                      "next_cursor": 1489467234237774933,
                      "next_cursor_str": "1489467234237774933",
                      "previous_cursor": 0,
                      "previous_cursor_str": "0"
                  }
                  )
    # Mocking response fot tweets
    responses.add(responses.GET,
                  'https://api.twitter.com/1.1/statuses/user_timeline.json?id=test_screen_name',
                  json=[
                      {
                          "created_at": "Thu Apr 06 15:28:43 +0000 2017",
                          "id_str": "850007368138018817",
                          "text": "I am not real",
                          "user": {
                              "id": 123,
                              "name": "test",
                              "screen_name": "test_screen_name",
                              "location": "nowhere",
                              "url": "localhost",
                              "description": "mocked_test_user",
                              "followers_count": 2
                          },
                          "entities": {
                              "hashtags": []}
                      },
                      {
                          "created_at": "Thu Apr 06 15:28:43 +0000 2017",
                          "id": 850007368138018817,
                          "id_str": "850007368138018817",
                          "text": "I am not real",
                          "user": {
                              "id": 123,
                              "name": "test",
                              "screen_name": "test_screen_name",
                              "location": "nowhere",
                              "url": "localhost",
                              "description": "mocked_test_user",
                              "followers_count": 2
                          },
                          "entities": {
                              "hashtags": []}
                      },
                      {
                          "created_at": "Thu Apr 06 15:28:43 +0000 2017",
                          "id": 850007368138018817,
                          "id_str": "850007368138018817",
                          "text": "I am not real",
                          "user": {
                              "id": 123,
                              "name": "test",
                              "screen_name": "test_screen_name",
                              "location": "nowhere",
                              "url": "localhost",
                              "description": "mocked_test_user",
                              "followers_count": 2
                          },
                          "entities": {
                              "hashtags": []}
                      },
                      {
                          "created_at": "Thu Apr 06 15:28:43 +0000 2017",
                          "id": 850007368138018817,
                          "id_str": "850007368138018817",
                          "text": "I am not real",
                          "user": {
                              "id": 123,
                              "name": "test",
                              "screen_name": "test_screen_name",
                              "location": "nowhere",
                              "url": "localhost",
                              "description": "mocked_test_user",
                              "followers_count": 2
                          },
                          "entities": {
                              "hashtags": []}
                      },
                      {
                          "created_at": "Thu Apr 06 15:28:43 +0000 2017",
                          "id": 850007368138018817,
                          "id_str": "850007368138018817",
                          "text": "I am not real",
                          "user": {
                              "id": 123,
                              "name": "test",
                              "screen_name": "test_screen_name",
                              "location": "nowhere",
                              "url": "localhost",
                              "description": "mocked_test_user",
                              "followers_count": 2
                          },
                          "entities": {
                              "hashtags": []}
                      },
                      {
                          "created_at": "Thu Apr 06 15:28:43 +0000 2017",
                          "id": 850007368138018817,
                          "id_str": "850007368138018817",
                          "text": "I am not real",
                          "user": {
                              "id": 123,
                              "name": "test",
                              "screen_name": "test_screen_name",
                              "location": "nowhere",
                              "url": "localhost",
                              "description": "mocked_test_user",
                              "followers_count": 2
                          },
                          "entities": {
                              "hashtags": []}
                      },
                  ]
                  )
    client = app.test_client()

    yield client
