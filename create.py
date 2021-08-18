#!python
print("content-type: text/html; charset=utf-8\n")
import cgi, view

form = cgi.FieldStorage()
if 'id' in form:
    pageId1 = form["id"].value
    desc1 = open('data/' + pageId, 'r').read()
else:
    pageId1 = 'Welcome'
    desc1 = 'Hello, web'

print('''<!DOCTYPE html>
<html>
<head>
  <title>WEB1 - Welcome</title>
  <meta charset="utf-8">
</head>
<body>
  <h1><a href="index.py">WEB</a></h1>
  <ol>
    {listStr2}
  </ol>
  <a href="create.py">create</a>
  <form action="process_create.py" method="post">
    <p><input type="text" name="title" placeholder="title"></p>
    <p><textarea rows="4" name="description" placeholder="description"></textarea></p>
    <p><input type="submit"></p>
  </form>
</body>
</html>
'''.format(listStr2 = view.getList()))
