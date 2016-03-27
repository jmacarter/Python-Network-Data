import re
numlist = list()

hand = open('regex_sum_200855.txt')
for line in hand:
    line = line.rstrip()
    words = line.split()
    for word in words:
        stuff = re.findall('^([0-9]+)',word)
        if len(stuff) != 1 : continue
        num = float(stuff[0])
        numlist.append(num)
print 'Sum: ', int(sum(numlist))




print sum( [int(y) for y in re.findall('[0-9]+',open('regex_sum_200855.txt').read()) ] )




 #
 #print sum( [ ****** *** * in **********('[0-9]+',**************************.read()) ] )
 #
