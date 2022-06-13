# Description
A tool designed to screenshot a web application's homepage from a list of URL's, domains or IP's. This tool was made mostly for use on pentests to run through a list of hosts and screenshot the webpage, if present, on the specified port(s).

# Usage
Put your IP addresses, URL's or domain names in a file, and pass it to the script. Optionally, you can specify ports to check on each host by using the '_--ports=_' argument. You can also ignore SSL certificate errors by specifying '_--ignore-ssl_'.

```
> python web-screenshotter.py url-list --ports=80,443,8080,8443 --ignore-ssl
```
An example of a list of hosts is as follows:
```
192.168.12.4
http://192.168.12.22
https://google.com/
spotify.com
https://10.0.4.54
```
## Options
```
usage: web-screenshotter.py [-h] [--ports PORTS] [--ignore-ssl] hosts

Website screenshot tool

positional arguments:
  hosts          File containing URL's, IP addresses, or a mix

optional arguments:
  -h, --help     show this help message and exit
  --ports PORTS  Specify which ports to try. Default is 80 is SSL is not detected, 443 if it is
  --ignore-ssl   Ignore certificate and other SSL-related errors
  ```
## Requirements
_selenium_ and _requests_, both available via pip. Also make sure _chromedriver_ is in your path. It's usually auto-added if installed via pacman, apt or brew.

### TODO's and Bug Fixes in Progress
- Implement multithreading for speed increase.
- Add support for when a user specifies a port on a host in the host list _and_ ports arguement.
