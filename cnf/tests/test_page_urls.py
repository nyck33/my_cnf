from flask import url_for

def test_page_urls(client):
    #visit home page
    response = client.get(url_for('main.home_page'), follow_redirects=True)
    assert response.status_code==200

    #login as user and visit user page
    response = client.post(url_for('user.login'), follow_redirects=True,
                           data=dict(email='user@example.com', password='Password1'))
    assert response.status_code==200
    response = client.get(url_for('main.member_page'), follow_redirects=True)
    assert response.status_code==200

    #edit user profile page
    response = client.get(url_for('main.user_profile_page'), follow_redirects=True)
    assert response==200
    response = client.post(url_for('main.user_profile_page'), follow_redirects=True,
                           data=dict(first_name='User', last_name='User'))
    assert response.status_code==200
    response = client.get(url_for('main.member_page'), follow_redirects=True)
    assert response.status_code==200

    #logout
    response = client.get(url_for('user.logout'), follow_redirects=True)
    assert response.status_code==200
