from flask import Flask
from flask import request
import json
import requests
import os

macaddress_url = 'https://api.macaddress.io/v1?apiKey={}&output={}&search={}'

if 'OUI_API_KEY' in os.environ:
    api_key = os.environ['OUI_API_KEY']
else:
    print('Please provide your API Key OUI_API_KEY environment var.  Sign up at https://macaddress.io/')
    exit()


def mac_lookup(api_key, output, mac):
    response = requests.get(macaddress_url.format(api_key, output, mac))
    return response.text


app = Flask(__name__)


@app.route('/macoui', methods=['GET', 'POST'])
def macoui():

    if request.method == 'POST':
        data = json.loads(request.data)
        mac_list = data['maclist']
        return_list = []
        for mac in mac_list:
            response = mac_lookup(api_key, 'vendor', mac)
            return_list.append({mac: response})
        return_data = {'response': return_list}
        return json.dumps(return_data)
    elif request.method == 'GET':
        mac = request.query_string.decode("utf-8")
        response = mac_lookup(api_key, 'vendor', mac)
        return_data = {'response': [{mac: response}]}
        return json.dumps(return_data)
    else:
        print('ERROR: Invalid method {}'.format(request.data))
        return 'ERROR: Invalid method {}'.format(request.data)


if __name__ == '__main__':
    # app.run(debug=True)
    app.run(host='0.0.0.0')
