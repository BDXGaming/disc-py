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


class BaseUser:

    def __init__(self, **kwargs):

        self._username = kwargs.pop("username", None)
        self._icon_url = kwargs.pop("icon_url", None)

    def __str__(self):
        return self._username

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, new_username: str):
        self._username = new_username

    @property
    def icon_url(self):
        return self._icon_url

    @icon_url.setter
    def icon_url(self, new_avatar_url: str):
        self._icon_url = new_avatar_url

    def to_dict(self):
        """
        Converts the cls to a dict that can be used for webhook embeds
        :return:
        """
        dict = {}

        if self._username is not None:
            dict['name'] = self._username

        if self._icon_url is not None:
            dict['icon_url'] = self._icon_url

        return dict
