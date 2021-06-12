# viewdns-python

`viewdns-python` is a Python library for interacting with the [ViewDNS.info](https://viewdns.info/) API.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install viewdns-python.

```bash
pip setup.py install
```

## Features

`viewdns-python` does not support all the tools *yet*. Below is a list of what is **currently supported**:

* DNS Record Lookup
* Get HTTP Headers
* IP Location Finder

## Usage

```python
import viewdns

client = viewdns.Client('your-api-key')

info = client.get_ip_location('127.0.0.1')

print(info) # {'query': {'tool': 'iplocation_PRO', 'ip': '127.0.0.1'}, 'response': {'city': '', 'zipcode': '0', 'region_code': '', 'region_name': '', 'country_code': 'JP', 'country_name': 'Japan', 'latitude': '35.69', 'longitude': '139.69', 'gmt_offset': '', 'dst_offset': ''}}
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