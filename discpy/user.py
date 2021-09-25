class baseUser:

    def __init__(self, **kwargs):

        self._username = kwargs['username']
        self._avatar_url = kwargs['avatar_url']

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, new_username:str):
        self._username = new_username

    @property
    def avatar_url(self):
        return self._avatar_url

    @avatar_url.setter
    def avatar_url(self, new_avatar_url:str):
        self._avatar_url = new_avatar_url

