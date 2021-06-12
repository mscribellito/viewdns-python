from .BaseObject import BaseObject

class IPLocation(BaseObject):

    def __init__(self, *args, **kwargs):
        
        self.city = None
        self.zipcode = None
        self.region_code = None
        self.country_code = None
        self.country_name = None
        self.latitude = None
        self.longitude = None
        self.gmt_offset = None
        self.dst_offset = None

        super(IPLocation, self).__init__(*args, **kwargs)
