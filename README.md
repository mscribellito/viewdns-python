# viewdns-python

`viewdns-python` is a Python library for interacting with the [ViewDNS.info](https://viewdns.info/) API.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install viewdns-python.

```bash
pip install viewdns-python
```

## Usage

```python
import viewdns

client = viewdns.Client('your-api-key')

print(client.get_ip_location('127.0.0.1'))
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