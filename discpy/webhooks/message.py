class messageMeta:

    @staticmethod
    def do_thing():
        pass

class Message(messageMeta):
    '''
    The message object for webhooks
    '''

    def __init__(self, **kwargs):

        self.content = kwargs['content']

        if("username" in kwargs.keys()):
            self.username = kwargs["username"]

        else:
            self.username = None

        if("avatar_url" in kwargs.keys()):
            self.avatar_url = kwargs['avatar_url']

        else:
            self.avatar_url = None

    def to_dict(self):
        '''
        Converts the message object into a dict
        :return:
        '''

        data = {}

        data['username'] = self.username

        if self.avatar_url != None:
            data['avatar_url'] = self.avatar_url

        data['content'] = self.content

        return data
