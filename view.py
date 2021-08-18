import os, sys
sys.path.append('C:/users/82105/appdata/roaming/python/python39/site-packages')
import html_sanitizer
sanitizer = html_sanitizer.Sanitizer()

def getList():
    files = os.listdir('data')
    listStr1 = ''
    for item in files:
        item = sanitizer.sanitize(item)
        listStr1 = listStr1 + '<li><a href="index.py?id={name}">{name}</a></li>'.format(name = item)
    return listStr1
