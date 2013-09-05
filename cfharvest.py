#!/bin/env/python

import optparse
import re
import mechanize
import os
from datetime import date
from BeautifulSoup import BeautifulSoup
import cookielib

# Store the current date in isoformat, YYYY-MM-DD, as a string
currentdate = str(date.today().isoformat())
# Since we want to harvest cloudflare changes, we'll just set it global
cf = "cloudflare.com"

URL = "http://www.dailychanges.com/%s/%s/" % (cf, currentdate)
URLdl = "http://www.dailychanges.com/export/%s/%s/export.csv" % (cf, currentdate)
fnam = currentdate + "daily.csv"

br = mechanize.Browser()
br.addheaders=[('User-agent', 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.17 Safari/537.36'),
("Referer", URL)]
br.set_handle_robots(False)
br.set_debug_http(True)
cj = cookielib.LWPCookieJar()
br.set_cookiejar(cj)
f = br.retrieve(URLdl, fnam)[0]
print f
