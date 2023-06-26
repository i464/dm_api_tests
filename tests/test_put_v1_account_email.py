import requests
from services.dm_api_account import DmApiAccount
def test_put_account_email():
    api = DmApiAccount(host='http://localhost:5051')
    json = {
            "login": "login45",
            "password": "login45",
            # "email": "test46@test.com" new email ?
        }
    response = api.account.put_v1_account_email(
        json=json
    )
    print(response)
