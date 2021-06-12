import requests

try:
    import urlparse
except ImportError:
    from urllib import parse as urlparse

class Client():

    base_url = 'https://api.viewdns.info/'
    api_key = None

    def __init__(self, api_key):

        self.api_key = api_key
    
    def get_dns_records(self, domain, record_type='ANY'):

        params = dict()
        params['domain'] = domain
        params['recordtype'] = record_type

        data = self._execute('dnsrecord', params=params)

        return data
    
    def get_ip_location(self, ip):

        params = dict()
        params['ip'] = ip

        data = self._execute('iplocation', params=params)

        return data
    
    def _execute(self, url, params=None):

        url = urlparse.urljoin(self.base_url, url)

        if params is None:
            params = dict()

        params['apikey'] = self.api_key
        params['output'] = 'json'

        req = requests.get(url, params=params)

        if req.status_code == 404:
            raise Exception()

        try:
            data = req.json()
        except ValueError as e:
            raise Exception(e)

        return data
