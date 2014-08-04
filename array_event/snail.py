# -*- coding: utf-8 -*-
snail_array = []

for i in range(5):
	empty_array = []
	for j in range(5):
		empty_array.append(0)
	snail_array.append(empty_array)

for column in snail_array:
	for num in column:
		print "%2s" % num,
	print
# print init array
 # 0  0  0  0  0
 # 0  0  0  0  0
 # 0  0  0  0  0
 # 0  0  0  0  0
 # 0  0  0  0  0

# change array like this
#  1  2  3  4 5
# 16 17 18 19 6
# 15 24 25 20 7
# 14 23 22 21 8
# 13 12 11 10 9 

######## insert your algorithm here ########


print 
for column in snail_array:
	for num in column:
		print "%2s" % num,
	print
# print result array
# 영어 주석 힘들다.