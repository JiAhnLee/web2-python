#!python

import cgi, os

form = cgi.FieldStorage()
pageId1 = form["pageId"].value
title1 = form["title"].value
desc1= form["description"].value

opened_file = open('data/' + pageId1, 'w')
opened_file.write(desc1)
opened_file.close()

os.rename('data/' + pageId1, 'data/' + title1)

#Redirection
print("Location: index.py?id=" + title1)
print()
