class baseUser:

    def __init__(self, **kwargs):

        self._username = kwargs.pop("username", None)
        self._icon_url = kwargs.pop("icon_url", None)

    def __str__(self):
        return self._username

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, new_username:str):
        self._username = new_username

    @property
    def icon_url(self):
        return self._icon_url

    @icon_url.setter
    def icon_url(self, new_avatar_url:str):
        self._icon_url = new_avatar_url

    def to_dict(self):
        '''
        Converts the cls to a dict that can be used for webhook embeds
        :return:
        '''
        dict = {}

        if self._username != None:
            dict['name'] = self._username

        if self._icon_url != None:
            dict['icon_url'] = self._icon_url

        return dict
