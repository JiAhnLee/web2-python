#!python

import cgi,os

form = cgi.FieldStorage()
pageId1 = form["pageId"].value

os.remove('data/' + pageId1)

#Redirection
print("Location: index.py")
print()
