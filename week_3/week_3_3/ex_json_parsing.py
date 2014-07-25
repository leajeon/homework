#-*- coding: utf-8 -*-
# json 파싱하기

import urllib
import json

htmltext = urllib.urlopen("http://codingsroom.com/likelion/json_example2.php")

data = json.load(htmltext)

print data
print "\n"
print "MEM_NUM   age       job       MEM_CODE     etc "
for i in data['data']:
	print "%4s %7s %13s %12s"%(i['MEM_NUM'], i['age'], i['job'], i['MEM_CODE']),
	if i['age'] > 50 :
		print "   old"
	else:
		print " "