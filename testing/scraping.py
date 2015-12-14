import re
import urllib.request

from time import sleep

#load page
page = urllib.request.urlopen('http://magiccards.info/sitemap.html')
html = page.read()
#get english language
lang_english = re.search(b'<a name="en">.+?</table>', html, flags=re.DOTALL).group()
#get block groups
en_block_groups = re.findall(b'<h3>([\w\s\'"-]+)</h3>(.+?)</li></ul></li></ul>', lang_english)
for block_group in en_block_groups:
    name, data = block_group
    sleep(5)
    print(name)
    sleep(1)
    print(data)
