#!python
print("content-type: text/html; charset=utf-8\n")
import cgi, view, sys
sys.path.append('C:/users/82105/appdata/roaming/python/python39/site-packages')
import html_sanitizer
sanitizer = html_sanitizer.Sanitizer()

form = cgi.FieldStorage()
if 'id' in form:
    title1 = pageId1 = form["id"].value
    desc1 = open('data/' + pageId1, 'r').read()
    # desc1 = desc1.replace('<', '&lt;')
    # desc1 = desc1.replace('>', '&gt;')
    title1 = sanitizer.sanitize(title1)
    desc1 = sanitizer.sanitize(desc1)
    update_link1 = '<a href="update.py?id={}">update</a>'.format(pageId1)
    delete_action1 = '''
                    <form action="process_delete.py" method="post">
                        <input type="hidden" name="pageId" value="{}">
                        <input type="submit" value="delete">
                    </form>
    '''.format(pageId1)
else:
    title1 = pageId1 = 'Welcome'
    desc1 = 'Hello, web'
    update_link1 = ''
    delete_action1 = ''

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
  {update_link2}
  {delete_action2}
  <h2>{title2}</h2>
  <p>{desc2}</p>
</body>
</html>
'''.format(
    title2 = title1,
    desc2 = desc1,
    listStr2 = view.getList(),
    update_link2 = update_link1,
    delete_action2 = delete_action1))
