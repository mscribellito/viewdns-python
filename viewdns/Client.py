import requests

try:
    import urlparse
except ImportError:
    from urllib import parse as urlparse

class Client():

    base_url = 'https://api.viewdns.info/'
    api_key = None

    def __init__(self, api_key):
        """
        Creates a new instance of the ViewDNS.info API client.

        The ViewDNS.info API allows webmasters to integrate the tools provided by ViewDNS.info into their own sites in a simple and effective manner.

        Docs: https://viewdns.info/api/docs/
        """

        self.api_key = api_key
    
    def get_dns_records(self, domain, record_type='ANY'):
        """
        View all configured DNS records (A, MX, CNAME etc.) for a specified domain name.

        Params:

        * domain - the domain name to lookup DNS records for

        * recordtype - the type of DNS record you wish to retrieve (default 'ANY')

        Docs: https://viewdns.info/api/docs/dns-record-lookup.php
        """

        params = dict()
        params['domain'] = domain
        params['recordtype'] = record_type

        data = self._execute('dnsrecord', params=params)

        return data
    
    def get_ip_location(self, ip):
        """
        This tool will display geographic information about a supplied IP address including city, country, latitude, longitude and more.
        
        Params:

        * ip - the ip address to find the location of

        Docs: https://viewdns.info/api/docs/ip-location-finder.php
        """

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
