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


class Message:
    """
    The message object for webhooks
    """

    def __init__(self, **kwargs):

        self.content = kwargs['content']

        if "username" in kwargs.keys():
            self.username = kwargs["username"]

        else:
            self.username = None

        if "avatar_url" in kwargs.keys():
            self.avatar_url = kwargs['avatar_url']

        else:
            self.avatar_url = None

    def to_dict(self):
        """
        Converts the message object into a dict
        :return:
        """

        data = {}

        if self.username is not None:
            data['username'] = self.username

        if self.avatar_url is not None:
            data['avatar_url'] = self.avatar_url

        data['content'] = self.content
        return data
