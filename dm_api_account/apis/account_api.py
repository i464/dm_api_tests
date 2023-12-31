import requests
from requests import Response
from ..models.reset_password_model import reset_password_model
from ..models.registration_model import registration_model
from ..models.change_email_model import change_email_model
from ..models.change_account_password_model import change_account_password_model
from requests import session
from restclient.restclient import Restclient

class AccountApi:
    def __init__(self,host,headers=None):
        self.host = host
        self.client = Restclient(host=host,headers=headers)
        if headers:
            self.client.session.headers.update(headers)


    def post_v1_account(self,json:registration_model,**kwargs) -> Response:
        """
        Register new user
        :param json: registration_model
        :return:
        """

        response = self.client.post(
            path = f"/v1/account",
            json=json,
            **kwargs
        )

        return response

    def post_v1_account_password(self,json:reset_password_model,**kwargs) -> Response:
        """
        Reset registered user password
        :param json: reset_password_model
        :return:
        """

        response = self.client.post(
            path = f"/v1/account/password",
            json=json,
            **kwargs
        )
        return response

    def put_v1_account_email(self,json:change_email_model,**kwargs) -> Response:
        """
        Change registered user email
        :param json: change_email_model
        :return:
        """

        response = self.client.put(
            path = f"/v1/account/email",
            json=json,
            **kwargs
        )
        return response

    def put_v1_account_password(self,json:change_account_password_model,**kwargs) -> Response:
        """
        Change registered user password
        :param json: change_account_password_model
        :return:
        """
        response = self.client.put(
            path=f"/v1/account/password",
            json=json,
            **kwargs
        )
        return response

    def put_v1_account_token(self,token:str,**kwargs)-> Response:
        """
        Activate registered user
        :param token:
        :return:
        """
        response = self.client.put(
            path = f"/v1/account/{token}",
            **kwargs
        )
        return response

    def get_v1_account(self,**kwargs)-> Response:
        """
        Get current user
        :return:
        """
        response = self.client.get(
            path = f"/v1/account",
            **kwargs

        )
        return response
