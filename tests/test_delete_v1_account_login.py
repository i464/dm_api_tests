import requests

from services.dm_api_account import DmApiAccount

# not ready
def test_delete_v1_account_login():
    api = DmApiAccount(host='http://localhost:5051')
    json = {
            "login": 'login45',
            "password": 'login45',
            "rememberMe": True
        }
    response = api.login.delete_v1_account_login(
        json=json
    )
    print(response)