import unittest
import responses
import viewdns

from .BaseTest import BaseTest

class TestDnsRecords(BaseTest):

    def setUp(self):
        
        super(TestDnsRecords, self).setUp()
        self.client = viewdns.Client(self.api_token)

    @responses.activate
    def test_get_dns_records(self):

        data = self.load_from_file('dns_records.json')

        url = self.base_url + 'dnsrecord'
        responses.add(responses.GET, url, body=data, status=200)

        dns_records = self.client.get_dns_records('twitter.com')

        self.assertEqual(dns_records[0].name, 'twitter.com.')
        self.assertEqual(dns_records[0].ttl, '30')
        self.assertEqual(dns_records[0].class_, 'IN')
        self.assertEqual(dns_records[0].type, 'A')
        self.assertEqual(dns_records[0].data, '199.59.148.82')

        self.assertEqual(dns_records[1].name, 'twitter.com.')
        self.assertEqual(dns_records[1].ttl, '600')
        self.assertEqual(dns_records[1].class_, 'IN')
        self.assertEqual(dns_records[1].type, 'MX')
        self.assertEqual(dns_records[1].priority, '10')
        self.assertEqual(dns_records[1].data, 'aspmx.l.google.com.')
