#! coding=utf-8
__date__   = '20160205'
__author__ = 'changgy'


''' define add function '''
class Cpython(object):
	cnt = 0
	
	def __init__(self, name):
		self.name = name
		
	def __input(self):
		list = []
		print "please input interger"
		
		while True :
			a = raw_input()
			if a == '.':
				break				
			list.append(eval(a))			
		return sum(list)
		
	def setName(self, name):
		self.name = name
		
	def getName(self):
		Cpython.cnt += 1
		print Cpython.cnt
		return self.name
''' end def '''
	
if __name__ == '__main__':
	me = Cpython('python go')
	me.__init__("te111")
	print me.__input()	
	#me.setName('python go')
	print me.getName()	
	
	me2 = Cpython('123go')		
	#me2.setName('123go')
	print me2.getName()
  