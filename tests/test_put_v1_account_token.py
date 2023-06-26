import requests
from services.dm_api_account import DmApiAccount


def test_put_v1_account_token(token="79fcb753-bad1-4100-94e2-658c0f4319bf"):
    api = DmApiAccount(host='http://localhost:5051')

    response = api.account.put_v1_account_token(token=token)

    print(response)


