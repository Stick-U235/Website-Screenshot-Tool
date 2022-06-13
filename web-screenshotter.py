import os
import sys
import argparse
from urllib.parse import urlparse
from http.client import HTTPConnection, HTTPSConnection
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from requests.exceptions import ConnectionError

# Arguement setup. Only URL list is required, port specification optional.
parser = argparse.ArgumentParser(description='Website screenshot tool')
parser.add_argument('hosts', type=argparse.FileType('r'),
                    help="File containing URL's, IP addresses, or a mix")
parser.add_argument('--ports', type=str, required=False,
                    help="Specify which ports to try. Default is 80 is SSL is not detected, 443 if it is")
args = parser.parse_args()

# Extracting port numbers from arg by splitting at the comma
d = vars(args)
if "ports" in d.keys() and args.ports:
    d["ports"] = [s.strip() for s in d["ports"].split(",")]
#print (args.ports)
url_file = args.hosts.readlines()


def parse_url_file():
  #Remove remove trailing newline and '/''s  
  urls_removed_newline = [x.replace('\n', '') for x in url_file]
  urls_removed_trailing_char = [item.strip("/") for item in urls_removed_newline]
  
  ports = args.ports
  final_url = []
  
  #Adding port numbers to each URL is ports were specified
  for index, item in enumerate(urls_removed_trailing_char, start=0):
      if ports:
          for index_b, item in enumerate(ports, start=0):
          #print(urls_formatted[index], ":", ports[index_b]) 
            final_url.append((urls_removed_trailing_char[index]) + ":" + str(ports[index_b]))
      else:
          #no ports specified
          final_url = urls_removed_trailing_char

  for x in final_url: 
     url_to_screenshot = x
     print("- Screenshotting URL: ", url_to_screenshot)
     take_screenshot(url_to_screenshot)



def check_ssl(url):
    HTTPS_URL = f'https://{url}'
    print("Checking SSL support on: ", HTTPS_URL)

    try:
        HTTPS_URL = urlparse(HTTPS_URL)
        connection = HTTPSConnection(HTTPS_URL.netloc, timeout=5)
        connection.request('HEAD', HTTPS_URL.path)
        if connection.getresponse():
            print("SSL is supported")
            return True
        else:
            print("SSL is not supported.")
            return False
    except:
        return False



def take_screenshot(url):
    print('Checking ' + url)

    #Selenium setup
    chrome_options = Options()
    driver_path_var = 'chromedriver'
    chrome_options.add_argument('--headless')
    chrome_options.add_argument("--window-size=1920x1080")
    driver = webdriver.Chrome(options=chrome_options, executable_path='chromedriver')
    driver.set_page_load_timeout(10) #Setting timeout, maybe make user modifiable as arg

    #Adding in approproate predending http protocol strings. This has a bug though,
    # only checks if ssl if string not present. So, http://google.com will not hit this.
    if 'https://' not in url and 'http://' not in url:
        if check_ssl(url):                                
          #SSL supported
          url = 'https://' + url
        else:
          #SSL unsupported
          url = 'http://' + url

        #print("Final URL to screenshot is: " + url)

    #take screenshot
    try:
        driver.get(url)
        save_screenshot(url, driver)
    except Exception as e:
        print("- Bad URL: ", url, "\nError info:")
        print(e.msg, "\n")

    driver.close() #Do I need this since I'm quitting it below?
    driver.quit()


def save_screenshot(url, driver):
    #Removing /'s for a cleaner screenshot title
    if "/" in url:
        remove_chars = ['/']
        filtered_chars = filter(lambda item: item not in remove_chars, url)
        screenshot_filename = ''.join(filtered_chars)

    print("Saving screenshot: ", url, '\n')
    screenshot_filename = screenshot_filename + '.png'
    screenshot = driver.save_screenshot(screenshot_filename)

def main():
    parse_url_file()

if __name__ == "__main__" :
    main()
