#-*- coding: utf-8 -*-
# JTBC 뉴스 속보 xml문서 파싱하기

import urllib
import webbrowser
from xml.etree.ElementTree import parse

xml = urllib.urlopen('http://www.hani.co.kr/rss/')	# 속보

tree = parse(xml)		# xml 파싱하여 나뭇가지 구조 얻기
root = tree.getroot()	# root태그 얻어오기

title_list = [ ]
number = 0

for parent in root.getiterator():	# root태그부터 시작하여 모든 태그를 반복
	for child in parent.findall("item"):	# item 태그를 모두 반복

		title_list.append(child)
		number += 1
		# 뉴스 제목 보기
#		print child.find("title").text
		print "%d"%(number) + " " + child.findtext("title")
		
		# 뉴스 내용 보기
#		print child.findtext("description")
print "\n"
select = int(raw_input("insert any number that you wanna read!"))

if select < 1 or select > 25:
	print "error! insert between 0 to 25"
elif select>=1 and select<=25:
	print "%d"%(select) + " " + "%s"%(title_list[select-1].findtext("title"))
	print "%d"%(select) + " " + "%s"%(title_list[select-1].findtext("link"))
	webbrowser.open(title_list[select-1].findtext("link"))

	#"%d"%(number) + " " + child.findtext("title")

