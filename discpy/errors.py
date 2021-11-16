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

class BadRequest(Exception):
    '''
    THis error is invoked when at bad HTTP request is made.
    '''

    def __init__(self):
        pass
    def __str__(self):
        return "Error 400 Bad Request"


class RequestTimeout(Exception):
    '''
    This error is thrown when a request timeout occurs
    '''
    def __int__(self):
        pass
    def __str__(self):
        return "Webhook request has timed out!"


class NoAddressGiven(Exception):
    """
    This error is raised when incomplete or incorrect webhook addresses are provided.
    """
    def __int__(self):
        pass
    def __str__(self):
        return "No address or incorrect details provided for webhook!"