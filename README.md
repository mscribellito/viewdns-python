# viewdns-python

`viewdns-python` is a Python library for interacting with the [ViewDNS.info](https://viewdns.info/) API.

[![Python package](https://github.com/mscribellito/viewdns-python/actions/workflows/python-package.yml/badge.svg)](https://github.com/mscribellito/viewdns-python/actions/workflows/python-package.yml)

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install viewdns-python.

```bash
pip setup.py install
```

## Usage

```python
import viewdns

client = viewdns.Client('your-api-key')
```

## Features

`viewdns-python` does not support all the tools *yet*. Below is a list of what is **currently supported**:

* [DNS Record Lookup](#dns-record-lookup)
* [Get HTTP Headers](#get-http-headers)
* [IP Location Finder](#ip-location-finder)

### DNS Record Lookup

```python
dns_records = client.get_dns_records('twitter.com')

print(dns_records) # [<DNSRecord> {name=twitter.com., ttl=293, class_=IN, type=SOA, priority=None, data=ns1.p26.dynect.net. zone-admin.dyndns.com. 2007158928 3600 600 604800 60, class=IN}, ...]
```

### Get HTTP Headers

```python
http_headers = client.get_http_headers('twitter.com')

print(http_headers) # [<HTTPHeader> {name=http_status, value=301}, ...]
```

### IP Location Finder

```python
ip_location = client.get_ip_location('11.11.11.11')

print(ip_location) # <IPLocation> {city=Bullard, zipcode=75757, region_code=TX, country_code=US, country_name=United States, latitude=32.1095, longitude=-95.3342, gmt_offset=, dst_offset=, region_name=Texas}
```

## Testing

### Docker

Build the container.

```
docker build -t viewdns-python-tests .
```

Run the tests.

```
docker run viewdns-python-tests
```

## Links

* [ViewDNS.info API Documentation](https://viewdns.info/api/docs/)

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)
