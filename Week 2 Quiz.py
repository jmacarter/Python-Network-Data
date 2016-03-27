#question 2
import re
x = '12345abc$10'
y = re.findall('\$+',x)
print 'Question 2: ',y

#question 3
import re
x = '12345abc'
y = re.findall('[a-z0-9]+',x)
print 'Question 3: ',y

#question 7
import re
x = '12345abc'
y = re.findall('[0-9]+',x)
print 'Question 7: ',y

#question 8
import re
x = 'From: Using the : character'
y = re.findall('^F.+:', x)
print 'Question 8: ',y

#question10
import re
x = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
y = re.findall('\S+?@\S+',x)
print 'Question 10: ',y
