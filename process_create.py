#!python

import cgi

form = cgi.FieldStorage()
title1 = form["title"].value
desc1 = form["description"].value

opened_file = open('data/' + title1, 'w')
opened_file.write(desc1)
opened_file.close()

#Redirection
print("Location: index.py?id=" + title1)
print()
