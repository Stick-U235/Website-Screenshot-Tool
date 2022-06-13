# Description
A tool designed to screenshot a web application's homepage from a list of URL's, domains or IP's. This tool was made mostly for use on pentests to run through a list of hosts and screenshot the webpage, if present, on the specified port(s).

# Usage
Put your IP addresses, URL's or domain names in a file, and pass it to the script. Optionally, you can specify ports to check on each host by using the '--ports=' arguement.

```
> python web-screenshotter.py url-list --ports=80,443,8080,8443
```
An example of a list of hosts is as follows:
```
192.168.12.4
192.168.12.22
https://google.com/
spotify.com
https://10.0.4.54
```
