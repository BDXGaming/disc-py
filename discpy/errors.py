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