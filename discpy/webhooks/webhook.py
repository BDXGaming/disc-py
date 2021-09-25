import requests
from requests import Timeout
from discpy.user import baseUser
from discpy import Embed
from discpy.errors import BadRequest, RequestTimeout
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
        self.user = baseUser(username= username, avatar_url = avatar_url)

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

            if (data["username"] == None and self.user.username !=None):
                data["username"] = str(self.user.username)

            if("avatar_url" not in data.keys()):
                data['avatar_url'] = self.user.avatar_url

        else:
            data = {}

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

        self.webhook = kwargs['webhook']
        self.user = self.webhook.user
        self.message = kwargs["message"]
        self.data = kwargs["data"]
        self.response = kwargs['response']

