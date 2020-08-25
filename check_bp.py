#!/usr/bin/python

import argparse
import requests
import sys
import time


URLS = {
    'get_info': 'http://{host}/v1/chain/get_info',
    'paused':   'http://{host}/v1/producer/paused'
}


def check_head_has_incremented(host, delay=7):
    url = URLS['get_info'].format(host=host)
    fst = requests.get(url, verify=False).json()
    time.sleep(delay)
    snd = requests.get(url, verify=False).json()
    if int(snd['head_block_num']) > int(fst['head_block_num']):
        return (0, 'OK')
    return (2, 'Head block number not incremented after delay')

def check_bp_paused(host):
    url = URLS['paused'].format(host=host)
    status = requests.post(url, verify=False).json()
    print(status)
    if status == True:
        return (0, 'Producer is paused')
    else:
        return (2, 'Producer is not paused')

ALLOWED_FUNCTIONS = {
    'check_head': check_head_has_incremented,
    'check_paused' : check_bp_paused
}

parser = argparse.ArgumentParser(description='chain info checker')
parser.add_argument('host', help='host address')
parser.add_argument('function', help='check to run', choices=ALLOWED_FUNCTIONS)



if __name__ == '__main__':
    args = parser.parse_args()

    func = ALLOWED_FUNCTIONS[args.function]
    try:
        exit_code, message = func(args.host)
    except requests.exceptions.RequestException:
        exit_code, message = (2, 'Error cannot connect to host ' + URLS['get_info'].format(host=args.host))
    except Exception as e:
        exit_code, message = (2, e.args[0])

    print(message)
    sys.exit(exit_code)
