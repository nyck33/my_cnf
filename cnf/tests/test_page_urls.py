"""
run tests with py.test cnf/tests --cov

"""

from flask import url_for
import json

def test_page_urls(client, db):
    #visit home page
    response = client.get(url_for('main.home_page'), follow_redirects=True)
    assert response.status_code==200

    #login as user and visit user page
    response = client.post(url_for('user.login'), follow_redirects=True,
                           data=dict(username='example_user', password='Password1'))
    assert response.status_code==200
    response = client.get(url_for('main.member_page'), follow_redirects=True)
    assert response.status_code==200

    #edit user profile page
    response = client.get(url_for('main.user_profile_page'), follow_redirects=True)
    assert response.status_code==200
    response = client.post(url_for('main.user_profile_page'), follow_redirects=True,
                           data=dict(first_name='User', last_name='User'))
    assert response.status_code==200

    response = client.get(url_for('main.member_page'), follow_redirects=True)
    assert response.status_code==200

    #test food search page
    response = client.get('/food_search?q=sugar', follow_redirects=True)
    assert response.status_code == 200
    data = response.get_data(as_text=True)
    print(data)
    assert 'Milk' in data

    response = client.get(url_for('main.food_search'), follow_redirects=True)
    assert response.status_code==200
    data = response.get_data(as_text=True)
    print(data)
    assert 'Canadian' in data
    #try searching for food
    food_choice = {'q': 'chocolate'}



    response = client.get(url_for('main.food_search'),
                           query_string=food_choice,
                           follow_redirects=True)
    assert response.status_code==200


    """make this random"""
    data = {'food_id' : 1}

    response = client.get(url_for('main.show'),
                          query_string=data,
                          follow_redirects=True)
    assert response.status_code==200
    #check html response data
    data = response.get_data(as_text=True)
    assert 'Conversions' in data

    #logout
    response = client.get(url_for('user.logout'), follow_redirects=True)
    assert response.status_code==200
