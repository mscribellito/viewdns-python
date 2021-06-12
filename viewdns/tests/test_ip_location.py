import unittest
import responses
import viewdns

from .BaseTest import BaseTest

class TestIpLocation(BaseTest):

    def setUp(self):
        
        super(TestIpLocation, self).setUp()
        self.client = viewdns.Client(self.api_token)

    @responses.activate
    def test_get_ip_location(self):

        data = self.load_from_file('ip_location.json')

        url = self.base_url + 'iplocation'
        responses.add(responses.GET, url, body=data, status=200)

        ip_location = self.client.get_ip_location('11.11.11.11')

        self.assertEqual(ip_location.city, 'Columbus')
        self.assertEqual(ip_location.zipcode, '43218')
        self.assertEqual(ip_location.region_code, 'OH')
        self.assertEqual(ip_location.region_name, 'Ohio')
        self.assertEqual(ip_location.country_code, 'US')
        self.assertEqual(ip_location.country_name, 'United States')
        self.assertEqual(ip_location.latitude, '39.9968')
        self.assertEqual(ip_location.longitude, '-82.9882')
        self.assertEqual(ip_location.gmt_offset, '')
        self.assertEqual(ip_location.dst_offset, '')
