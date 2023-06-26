
from services.dm_api_account import DmApiAccount
def test_put_v1_account_password():
    api = DmApiAccount(host='http://localhost:5051')
    json = {
            "login": "login45",
            "token": "79fcb753-bad1-4100-94e2-658c0f4319bf",
            "oldPassword": "login45",
            "newPassword": "login46"
        }
    response = api.account.put_v1_account_password(
        json=json
    )
    print(response)

