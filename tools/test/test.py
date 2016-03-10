# -*-Coding:utf-8 -*-

import urllib2
import re

tempStr = aStr.split('\"')[1]
if tempStr.istitle():
	print 'it is title format'
else:
	print 'it is not title format'


'''
dStr = urllib2.urlopen('http://finance.yahoo.com/q/cp?s=%5EDJI+Components').read()
m = re.findall('<tr><td class=\'yfnc_tabledata1\'><b><a href=\'.*?\'>\   	(.*?)</a></b></td><td class=\'yfnc_tabledata1\'> 	(.*?)</td>.*?<b>(.*?)</b>.*?</tr>', dStr)
if m:
    print m
    print '\n'
    print len(m)
else:  
    print 'not match'

readFile = open(r"src.txt", "r+")
lines = readFile.readlines()
for i in xrange( 0,len(lines)): 
	lines[i] = str(i+1) + " " + lines[i]	
readFile.close()


#write to file
output = open(r"des.txt","w")
output.write("How many roads must a man walk down\nBefore they call him a man\n")
for i in xrange(0,len(lines)):
	print lines[i]
	output.write(lines[i])	
#output.writelines(lines)
output.close()
'''