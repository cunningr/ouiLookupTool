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

The app uses plain HTTP providing no authenticity for users, the service itself or integrity of data exchanged.  A simple way to improve the security posture of the app would be to run it behind a proxy (E.g. nginx) providing HTTPS and if necessary validating client certs.

In a kubernetes context, this could be run in a Pod alongside an nginx container and the app code itself could be adjusted to listen only on localhost (127.0.0.1).  The nginx container would forward all requests to the App URL and redirect any other 'bad URL' request to an appropriate error page.

Nginx is a 'battle hardened', industry standard in Opensource web servers and _could_, deployed correctly, significantly improve the security posture of the App from the network point of view.

The App container itself is built on top of the Docker Python image ```python:3.8-slim-buster``` which provides security patches from the popular Debian release.  The Python requirements file specifies exact and current versions of the required python libraries in order to provide a known security posture.  For use in a secure environment we would recommend scanning container images as part of the CI build process using something like [anchore](https://anchore.com/).




