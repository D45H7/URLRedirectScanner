#!/usr/bin/python3.9

from io import BytesIO
import pycurl,sys

headers = {}

def display_header(header_line):
    header_line = header_line.decode('iso-8859-1')

    if ':' not in header_line:
        return

    h_name, h_value = header_line.split(':', 1)
    h_name = h_name.strip()
    h_value = h_value.strip()
    h_name = h_name.lower()
    h_value = h_value.lower()
    headers[h_name] = h_value

def main(url):
    b_obj = BytesIO()
    crl = pycurl.Curl()
    crl.setopt(crl.URL, url)
    crl.setopt(crl.HEADERFUNCTION, display_header)
    crl.setopt(crl.WRITEDATA, b_obj)
    crl.perform()

    print('Status:',crl.getinfo(crl.HTTP_CODE))

    if crl.getinfo(crl.HTTP_CODE) == 301:
      print('The URL is redirect to:',headers['location'])
    else:
      print('URL is not redirect, it safe!')

    print('=' * 20)

print("=== URL Redirection Scanner ===")
if len(sys.argv) == 2:
  main(sys.argv[1])
else:
  print("""===       by: EycAug10      ===
===============================

USAGE:
	python udirect.py [URL]
EXAMPLE:
	python udirect.py https://bit.ly/39qIO22 
""")

