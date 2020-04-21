# ouiLookupTool

ouiLookupTool is simple tool for resolving MAC addresses to get the OUI Vendor.  It uses the API hosted at [https://macaddress.io/](https://macaddress.io/) and has been containerised for convenient usage.  You will need to signup to the service (it's free) to receive your own unique API key.

To build the container (replacing the tag value if you wish);

```
docker build ./ --tag macoui
```

The tool runs in a container as a web service on http port 5000.  You can start the container like so, replacing your api key:

```
docker run --rm -e OUI_API_KEY='<your_api_key>' -p 5000:5000 macoui:latest
```

This will run the container in the foreground, exposing port 5000 through to the web app.

You can then use curl to query MAC OUIs with GET for individual MAC;

```
curl -X GET http://127.0.0.1:5000/macoui?44:38:39:ff:ef:57
```

Or POST with a list of MACs in a JSON list;

```
curl -X POST -H "Content-Type: application/json" -d '{"maclist": ["44:38:39:ff:ef:57", "44:38:39:ff:ef:57", "44:38:39:ff:ef:57", "44:38:39:ff:ef:57"]}' http://127.0.0.1:5000/macoui
```

## A note on security

The app uses plain HTTP providing no authentication or integrity of data.  I simple way to improve the security posture of the app would be to run it behind a proxy (E.g. nginx) providing HTTPS and if necessary validating client certs.


