import re

def cb(m):
	if m.group(0) == '&amp;':
		return '&'
	elif m.group(0) == '&gt;':
		return '>'
	elif m.group(0) == '&lt;':
		return '<'
	elif m.group(0) == '&nbsp;':
		return ' '

rexp = re.compile('<title>(.+?)</title>')
rexp1 = re.compile('<!--.*?-->',re.DOTALL)
rexp2 = re.compile(r'<(s(?:cript|tyle)).*?>.*?</\1>',re.DOTALL)
rexp3 = re.compile('<a.*?href="(.+?)".*?>(.*?)</a>',re.DOTALL)
rexp4 = re.compile('<.*?>',re.DOTALL)
rexp5 = re.compile(r'&(amp|gt|lt|nbsp);')
rexp6 = re.compile(r'\s+')

with open('testpage.txt','r') as fp:
	text = fp.read()
  
	for m in rexp.finditer(text):
		print(m.group(1))
		
	text = rexp1.sub(' ',text)
	text = rexp2.sub(' ',text)
		
	for m in rexp3.finditer(text):
		print(m.group(1),m.group(2))
		
	text = rexp4.sub(' ',text)
	text = rexp5.sub(cb,text)
	text = rexp6.sub(' ',text)

	print(text)
