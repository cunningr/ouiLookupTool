import requests
import argparse
import os

macaddress_url = 'https://api.macaddress.io/v1?apiKey={}&output={}&search={}'

parser = argparse.ArgumentParser()
parser.add_argument("--mac", help="MAC address to lookup")
parser.add_argument("--api-key", help="API key. May also be provided by environment OUI_API_KEY")
parser.add_argument("--file", help="Text file containing a list of MAC addresses - one per line")
parser.add_argument("--output", default='vendor', help="supported outputs vendor(default)|json|xml|csv")
args = parser.parse_args()

if 'OUI_API_KEY' in os.environ:
    api_key = os.environ['OUI_API_KEY']
elif args.api_key:
    api_key = args.api_key
else:
    print('Please provide your API Key either via --api-key arg or OUI_API_KEY environment var')
    exit()


def main():

    if args.output not in ['vendor', 'json', 'xml', 'csv']:
        print('--output must be one of the following vendor(default)|json|xml|csv see -h for help')
        exit()

    if args.file:
        with open(args.file, 'r') as file:
            mac_list = file.readlines()

        for mac in mac_list:
            response = mac_lookup(api_key, args.output, mac)
            data = {'MAC': mac.strip(), 'RESPONSE': response}
            print_output(data, args.output)
    elif args.mac:
        response = mac_lookup(api_key, args.output, args.mac)
        data = {'MAC': args.mac, 'RESPONSE': response}
        print_output(data, args.output)
    else:
        print('Please provide either --mac or --file or use -h for help')
        exit()


def mac_lookup(api_key, output, mac):
    response = requests.get(macaddress_url.format(api_key, output, mac))
    return response.text


def print_output(data, output):
    if output == 'vendor':
        print('MAC: {}, Vendor: {}'.format(data['MAC'], data['RESPONSE']))
    else:
        print(data['RESPONSE'])


if __name__ == "__main__":
    main()
