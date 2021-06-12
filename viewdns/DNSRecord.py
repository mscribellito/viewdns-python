from .BaseObject import BaseObject

class DNSRecord(BaseObject):

    def __init__(self, *args, **kwargs):
        
        self.name = None
        self.ttl = None
        self.class_ = None
        self.type = None
        self.priority = None
        self.data = None

        super(DNSRecord, self).__init__(*args, **kwargs)
