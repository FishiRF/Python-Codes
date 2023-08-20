import pytest
import requests


# Get Existing User:
# 	Description: Test if you can retrieve details of an existing user.
# 	Request: GET https://reqres.in/api/user/1
# 	Expected Result: Response status code should be 200 and contain user data.

#  pytest fixture to get the user data from the API
@pytest.fixture
def user_data():
    url = 'https://reqres.in/api/user/1'
    res = requests.get(url)
    return res


# Test function using the user_data fixture
def test_user_data_status_code(user_data):
    assert user_data.status_code == 200


def test_user_data_content(user_data):
    user_data_json = user_data.json()
    expected_data = {
        "data": {
            "id": 1,
            "name": "cerulean",
            "year": 2000,
            "color": "#98B2D1",
            "pantone_value": "15-4020"
        },
        "support": {
            "url": "https://reqres.in/#support-heading",
            "text": "To keep ReqRes free, contributions towards server costs are appreciated!"
        }
    }
    assert user_data_json == expected_data


# ----------------------------------------------------------------------------
# Create User:
# 	Description: Test if you can successfully create a new user.
# 	Request: POST https://reqres.in/api/user with JSON payload containing user data.
# 	Expected Result: Response status code should be 201, and the returned data should match the submitted data.


# ----------------------------------------------------------------------------
# Login Successful:
# 	Description: Test if you can successfully log in with valid credentials.
# 	Request: POST https://reqres.in/api/login with valid login data.
# 	Expected Result: Response status code should be 200, and a token should be present in the response.


# ----------------------------------------------------------------------------
# Login Unsuccessful:
# 	Description: Test if login fails with incorrect credentials.
# 	Request: POST https://reqres.in/api/login with incorrect login data.
# 	Expected Result: Response status code should be 400.













