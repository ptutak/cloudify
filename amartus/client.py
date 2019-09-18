import sys
import argparse
import socket
import json
from uuid import getnode
from urllib.request import urlopen, Request
from urllib.parse import urljoin
from urllib.error import HTTPError


def parse_args(args=sys.argv[1:]):
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'server_address',
        help='Server address'
    )
    parser.add_argument(
        '-n',
        '--name',
        help='Name',
        default=''
    )
    parser.add_argument(
        '-u',
        '--userdata',
        help='Userdata',
        default=''
    )
    return parser.parse_args(args)


def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('10.255.255.255', 1))
        ip = s.getsockname()[0]
    except Exception:
        ip = '127.0.0.1'
    finally:
        s.close()
    return ip


def main():
    args = parse_args()
    new_register_request = Request(
        urljoin(args.server_address, '/ztp/register/{}'.format(getnode())),
        data=json.dumps({
            "ip": get_ip(),
            "name": args.name,
            "userdata": args.userdata
        }).encode(),
        method='PUT',
        headers={'Content-type': 'application/json'}
    )
    try:
        response = urlopen(new_register_request)
    except HTTPError:
        print('register conflict')
        return 1
    print(json.loads(response.read().decode()))
    return 0


if __name__ == '__main__':
    exit(main())
