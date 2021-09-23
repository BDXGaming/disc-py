import json
import requests

from discpy import Embed
from discpy.webhooks.message import Message


class webhookMeta:
    '''
    The metaInfo class behind the webhook. Contains and manages the address attr for the webhook
    '''

    def __init__(self, **kwargs):

        if kwargs.keys().__contains__("address"):

            self._address = kwargs['address']

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value


class webhook(webhookMeta):
    '''
    The main webhook class.
    '''

    def __init__(self, address:str, username:str = None, avatar_url:str = None):
        '''
        Creates a new instance of the webhook object
        :param address:
        :param username:
        :param avatar_url:
        '''
        super().__init__(address=address)
        self.username = username
        self.avatar_url = avatar_url

    def change_url(self, new_url):
        '''
        Changes the webhook url.
        :param new_url:
        :return:
        '''
        self.address = new_url

    def send(self, message:Message = None, view_raw_data:bool = False, embed:Embed = None):
        '''
        When invoked
        :param message: A message object
        :return:
        '''

        if(message != None):

            data = message.to_dict()

            if (data["username"] == None and self.username !=None):
                data["username"] = str(self.username)

            if("avatar_url" not in data.keys()):
                data['avatar_url'] = self.avatar_url

        else:
            data = {}

        if(embed != None):
            edata = embed.to_dict()

            data["embeds"] = [edata]

        if (view_raw_data == True):
            print(data)


        result = requests.post(url=self.address, json=data)

        if result.status_code != 204:
            print(result)

        return sentWebhook(address=self.address, data=data, message=message, response=result)

class sentWebhook(webhook):

    def __init__(self, address: str, **kwargs):

        if("username" in (kwargs["data"]).keys()):
            super().__init__(address=address, username=(kwargs['data'])['username'])

        else:
            super().__init__(address=address)

        self.message = kwargs["message"]
        self.data = kwargs["data"]
        self.resp = kwargs['response']

