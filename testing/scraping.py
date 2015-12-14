import re
import urllib2

from math import ceil
from time import sleep

page = urllib2.urlopen('http://magiccards.info/sitemap.html')
html = page.read()
english = re.search('<a name="en">.+?</table>', html, flags=re.DOTALL)
'''
lines = [english.group()[line*80:line*80+80] \
        for line in range(int(ceil(len(english.group()) / 80.0)))]
for line in lines:
    print line
    sleep(0.1)
'''
en_groups = re.findall('<h3>[\w\s]+</h3>', english.group())
for match in en_groups:
    print match
