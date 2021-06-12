import requests

try:
    import urlparse
except ImportError:
    from urllib import parse as urlparse

from .DNSRecord import DNSRecord
from .HTTPHeader import HTTPHeader
from .IPLocation import IPLocation

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

        res = self._execute('dnsrecord', params=params)

        dns_records = []

        for dns_record in res['response']['records']:
            # class is a reserved word :|
            dns_record['class_'] = dns_record['class']
            dns_record = DNSRecord(**dns_record)
            dns_records.append(dns_record)

        return dns_records
    
    def get_http_headers(self, domain):
        """
        Retrieves the HTTP headers of a remote domain. Useful in determining the web server (and version) in use and much more.

        Params:

        * domain - the domain to retrieve the HTTP headers for

        Docs: https://viewdns.info/api/docs/get-http-headers.php
        """

        params = dict()
        params['domain'] = domain

        res = self._execute('httpheaders', params=params)

        http_headers = []

        for http_header in res['response']['headers']:
            http_header = HTTPHeader(**http_header)
            http_headers.append(http_header)

        return http_headers
    
    def get_ip_location(self, ip):
        """
        This tool will display geographic information about a supplied IP address including city, country, latitude, longitude and more.
        
        Params:

        * ip - the ip address to find the location of

        Docs: https://viewdns.info/api/docs/ip-location-finder.php
        """

        params = dict()
        params['ip'] = ip

        res = self._execute('iplocation', params=params)

        ip_location = IPLocation(**res['response'])

        return ip_location
    
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
