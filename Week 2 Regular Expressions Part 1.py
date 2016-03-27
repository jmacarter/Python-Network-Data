# #original method
# print "Original method: "
# hand = open('mbox-short.txt')
# for line in hand:
#     line = line.rstrip()
#     if line.find('From: ') >= 0:
#         print line
#
#
# #with regex
# print "With Regular Expressions: "
# import re
# hand = open('mbox-short.txt')
# for line in hand:
#     line = line.rstrip()
#     if re.search('From: ', line):
#         print line


# #original method
# print "Original method: "
# hand = open('mbox-short.txt')
# for line in hand:
#     line = line.rstrip()
#     if line.startswith('From: ') :
#         print line
#
#
# #with regex
# print "With Regular Expressions and carat: "
# import re
# hand = open('mbox-short.txt')
# for line in hand:
#     line = line.rstrip()
#     if re.search('^From: ', line):
#         print line

#with regex
# print "Regular Expressions and wildcard: "
# import re
# hand = open('mbox-short.txt')
# for line in hand:
#     line = line.rstrip()
#     if re.search('^X-\S+:', line):
#         print line

# import re
# x = 'My 2 favorite numbers are 19 and 42'
# y = re.findall('[0-9]+',x) #returns a python list
# print y
#
# y = re.findall('[AEIOU]+',x) #uppercase vowels
# print y #empty list - no uppercase vowels

import re
x = 'From: Using the : character'
y = re.findall('^F.+:',x) #greedy matching - largest match
print y
z = re.findall('^F.+?:',x) #non-greedy matching, shortest match
print z
