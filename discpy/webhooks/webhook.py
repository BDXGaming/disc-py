"""
MIT License

Copyright (c) 2021 BDXGaming

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import requests
from requests import Timeout
from discpy.user import baseUser
from discpy import Embed
from discpy.errors import BadRequest, RequestTimeout, NoAddressGiven
from discpy.webhooks.message import Message


class webhookMeta:
    '''
    The metaInfo class behind the webhook. Contains and manages the address attr for the webhook
    '''

    def __init__(self, **kwargs):
        _addressFormatBase = "https://discord.com/api/webhooks/"

        if kwargs.keys().__contains__("address"):

            if(kwargs['address'].__contains__(_addressFormatBase[:-8])):
                webhook_index = (kwargs['address']).index("webhooks/")
                webhook_data = (kwargs['address'])[webhook_index+9:]

                webhook_id = webhook_data[:webhook_data.index("/")]
                webhook_token = webhook_data[webhook_data.index("/")+1:]

                self._address = _addressFormatBase + f"{webhook_id}/{webhook_token}"

            else:
                raise NoAddressGiven

        elif kwargs.keys().__contains__("webhook_id") and kwargs.keys().__contains__("webhook_token"):

            self._address = _addressFormatBase + f"{kwargs['webhook_id']}/{kwargs['webhook_token']}"

        else:
            raise NoAddressGiven

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
        self.user = baseUser(username= username, icon_url = avatar_url)

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

            if ("username" not in data.keys()):
                data["username"] = str(self.user.username)

            if("avatar_url" not in data.keys()):
                data['avatar_url'] = self.user.icon_url

        else:
            data = {}

            if ("username" not in data.keys()):
                data["username"] = str(self.user.username)

            if("avatar_url" not in data.keys()):
                data['avatar_url'] = self.user.icon_url

        if(embed != None):
            edata = embed.to_dict()

            data["embeds"] = [edata]

        if (view_raw_data == True):
            print(data)

        try:
            result = requests.post(url=self.address, json=data, timeout=2)
        except Timeout:
            raise RequestTimeout

        if result.status_code != 204:
            print(result)

            if(result.status_code == 400):
                raise BadRequest

        return sentWebhook(data=data, message=message, response=result, webhook = self)

class sentWebhook():

    def __init__(self, **kwargs):
        '''
        Creates a new instance of the sent webhook object.
        :param kwargs:
        '''
        self.webhook = kwargs['webhook']
        self.user = self.webhook.user
        self.message = kwargs["message"]
        self.data = kwargs["data"]
        self.response = kwargs['response']

