# import re
# hand = open('mbox-short.txt')
# for line in hand:
#     line = line.rstrip()
#     if re.search('From: ', line):
#         y = line.strip()
#         if re.findall('\S+@\S+', y):
#             print re.findall('\S+@\S+', y)


# data = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
# atpos = data.find('@')
# print atpos
#
# sppos = data.find(' ',atpos)
# print sppos
#
# host = data[atpos+1 : sppos]
# print host


# import re
# hand = open('mbox-short.txt')
# for line in hand:
#     line = line.rstrip()
#     if re.search('From: ', line):
#         words = line.split()
#         email = words[1]
#         pieces = email.split('@')
#         print pieces[1]


# import re
# lin = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
# y = re.findall('@([^ ]*)', lin)
# print y


# import re
# lin = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
# y = re.findall('^From .*@([^ ]*)', lin)
# print y

# import re
# hand = open('mbox-short.txt')
# numlist = list()
# for line in hand:
#     line = line.rstrip()
#     stuff = re.findall('^X-DSPAM-Confidence: ([0-9.]+)',line) #inside a bracket, period isn't a wild card
#     if len(stuff) != 1 : continue
#     num = float(stuff[0])
#     numlist.append(num)
# print 'Maximum: ', max(numlist)

import re
x = 'We just received $10.00 for cookies.'
y = re.findall('\$[0-9.]+',x) #preface $ with \ to refer to the actual dollar sign character
print y
