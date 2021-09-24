class BadRequest(Exception):
    '''
    THis error is invoked when at bad HTTP request is made.
    '''

    def __init__(self):
        pass
    def __str__(self):
        return "Error 400 Bad Request"