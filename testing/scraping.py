import re
import urllib.request

from time import sleep

#load page
page = urllib.request.urlopen('http://magiccards.info/sitemap.html')
html = page.read()
#get english language
lang_english = re.search(b'<a name="en">.+?</table>', html, flags=re.DOTALL).group()
print(lang_english)
print('\n\n' + '-'*35 + '  BREAK  ' + '-'*35 + '\n')
#get block groups
#en_block_groups = re.findall(b'<h3>([\w\s\'"-]+)</h3>(.+?)</li></ul></li></ul>', lang_english)
en_block_groups = re.findall(b'<h3>([\w\s\'"-]+)</h3>(.+?)</td>', lang_english)
for block_group in en_block_groups:
    name, data = block_group
    print(name)
    print(data)
    print()
print('\n\n' + '-'*35 + '  BREAK  ' + '-'*35 + '\n')
for block_group in en_block_groups:
    _, data = block_group
    blocks = re.findall(b'<li>([\w\s\'":-]+)<ul><li>(.+?)</li></ul></li>|</small>$', data)
    for block in blocks:
        name, set_data = block
        print(name)
        print(set_data)
        print()
