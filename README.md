# ouiLookupTool

ouiLookupTool is simple tool for resolving MAC addresses to get the OUI Vendor.  It uses the API hosted at [https://macaddress.io/](https://macaddress.io/) and has been containerised for convenient usage.  You will need to signup to the service (it's free) to receive your own unique API key.

To build the container (replacing the tag value if you wish);

```
docker build ./ --tag macoui
```

To run a basic MAC lookup, you can use the container like so, replacing your api key;

```
docker run --rm -e CMD='--mac 44:38:39:ff:ef:57' -e OUI_API_KEY='<your_api_key>' macoui:latest
```

You can alternatively select from the more detailed outputs of json,xml or csv using the ```--output``` argument;

```
docker run --rm -e CMD='--mac 44:38:39:ff:ef:57 --output json' -e OUI_API_KEY='<your_api_key>' macoui:latest
```

If you have multiple MAC addresses to lookup you can place this in a file with one MAC per line and provide the file as argument to the script.  You will also have to mount the directory where the file is located into the container and provide the full path (inside the container) to the file;

```
docker run --rm -e CMD='--mac 44:38:39:ff:ef:57 --file /mnt/macfile' -e OUI_API_KEY='<your_api_key>' -v ${PWD}:/mnt macoui:latest
```


