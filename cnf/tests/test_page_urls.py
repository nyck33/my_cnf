"""
run tests with py.test cnf/tests --cov

"""

from flask import url_for, current_app as app
import json
import pymongo

def test_page_urls(client, db):
    with app.app_context(), app.test_request_context():
        #visit home page
        response = client.get(url_for('main.home_page'), follow_redirects=True)
        assert response.status_code==200
        # register user
        response = client.post(url_for('user.register'), follow_redirects=True,
                               data=dict(username='example_user', password='Password1'))
        assert response.status_code == 200
        # check that I'm back on home page after 302 redirect
        data = response.get_data(as_text=True)
        assert 'Home' in data
        # log out and log in
        # logout
        response = client.get(url_for('user.logout'), follow_redirects=True)
        assert response.status_code == 200
        data = response.get_data(as_text=True)
        assert 'Home' in data

        #login as user and visit user page but link not on member page
        response = client.post(url_for('user.login'), follow_redirects=True,
                               data=dict(username='example_user', password='Password1'))
        assert response.status_code==200
        #redirects to member page
        data = response.get_data(as_text=True)
        assert 'Member' in data

        # go to register page and check the user profile page
        #edit user profile page
        response = client.get(url_for('main.user_profile_page'), follow_redirects=True)
        assert response.status_code==200
        response = client.post(url_for('main.user_profile_page'), follow_redirects=True,
                               data=dict(first_name='User', last_name='User'))
        assert response.status_code==200

        response = client.get(url_for('main.member_page'), follow_redirects=True)
        # redirects to home page
        assert response.status_code==200
        data = response.get_data(as_text=True)
        assert 'Home' in data

        #test food search page
        food_item = {'q': 'chocolate'}
        response = client.get(url_for('main.food_search'), query_string=food_item,
                              follow_redirects=True)
        assert response.status_code == 200
        data = response.get_data(as_text=True)
        print(data)
        assert 'Milk' in data

        # todo: make this random
        data = {'food_id' : '69'}
        response = client.get('/69')

        assert response.status_code==200
        #check html response data
        data = response.get_data(as_text=True)
        assert 'Conversions' in data

        #logout
        response = client.get(url_for('user.logout'), follow_redirects=True)
        assert response.status_code==200


def test_users(db):
    assert db['users']
    assert db.users
    print(db.users)

    test_user = 'example_user'
    all_users = db.users.find()
    # check password
    for user in all_users:
        if user['username'] == test_user:
            assert user.password == 'Password1'

def tear_down(db):
    # delete example_user from user collection
    user_coll = db.users
    myquery = {"username": "example_user"}
    user_coll.delete_one(myquery)
    #check that it is gone
    all_users = db.users.find()
    # check password
    for user in all_users:
        assert user['username'] != "example_user"
