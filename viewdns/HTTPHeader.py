from .BaseObject import BaseObject

class HTTPHeader(BaseObject):

    def __init__(self, *args, **kwargs):
        
        self.name = None
        self.value = None

        super(HTTPHeader, self).__init__(*args, **kwargs)
