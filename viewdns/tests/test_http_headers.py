import unittest
import responses
import viewdns

from .BaseTest import BaseTest

class TestHttpHeaders(BaseTest):

    def setUp(self):
        
        super(TestHttpHeaders, self).setUp()
        self.client = viewdns.Client(self.api_token)

    @responses.activate
    def test_get_dns_records(self):

        data = self.load_from_file('http_headers.json')

        url = self.base_url + 'httpheaders'
        responses.add(responses.GET, url, body=data, status=200)

        ip_location = self.client.get_http_headers('twitter.com')

        self.assertEqual(ip_location['query']['tool'], 'httpheaders_PRO')
        self.assertEqual(ip_location['query']['domain'], 'twitter.com')

        self.assertEqual(ip_location['response']['headers'][0]['name'], 'http_status')
        self.assertEqual(ip_location['response']['headers'][0]['value'], '301')

        self.assertEqual(ip_location['response']['headers'][8]['name'], 'x-response-time')
        self.assertEqual(ip_location['response']['headers'][8]['value'], '2')
