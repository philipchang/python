#！/bin/env python
# coding=utf-8


#####################################
# heap sort
# author: changgy
# date: 2016-04-07
#####################################

import random

# based max heap, the index  0 is invalid, valid is [1, n]
class heapSort(object):
	
	# init
	def __init__(self, srcarray):
		self.m_array = srcarray
		self.maxIndex = len(srcarray) - 1
	
	# move the index item up
	def swapUp(self, index):
		i = index
		while ((i > 1) and (self.m_array[i] > self.m_array[i / 2]) ):
				self.m_array[i], self.m_array[i / 2] = self.m_array[i /2 ] , self.m_array[i]
				i >>= 1
				
	# move the index item down
	def swapDown(self, index):
		i = index * 2
		while( i <=  self.maxIndex):			
			if((i + 1) <=  self.maxIndex and self.m_array[i + 1] > self.m_array[i]):
				i += 1
			if(self.m_array[i] > self.m_array[i / 2]):
				self.m_array[i], self.m_array[i / 2] = self.m_array[i /2 ] , self.m_array[i]
			else:
				break
			i = i * 2
		
	
	# insert one item
	def insert(self, x):
		self.maxIndex += 1
		self.m_array.append( x )
		
		heapSort.swapUp(self, self.maxIndex)
		
	# del one item
	def delitem(self, index):

		self.m_array[index] = self.m_array[self.maxIndex]
		del self.m_array[self.maxIndex]
		self.maxIndex -= 1
		
		i = index
		if(i > 1 and self.m_array[i] > self.m_array[i / 2]):
			heapSort.swapUp(self, i)
		else:
			heapSort.swapDown(self, i)	
		
	# make the max heap, swapdown from maxindex / 2 to 1
	def makeHeap(self):
		arindex = [ (x+1) for x in xrange(self.maxIndex / 2) ]
		arindex.reverse()		
		for i in arindex :
			heapSort.swapDown(self, i)		
			
	# sort based on up 
	def sortData(self):		
		heapSort.makeHeap(self)
		
		maxnum = self.maxIndex		
		arindex = [ (x+1) for x in xrange(self.maxIndex) ]		
		arindex.reverse()
		for i in arindex:
			self.m_array[i], self.m_array[1] = self.m_array[1] , self.m_array[i]
			self.maxIndex -= 1 # move the current max item to the last one, then max index small
			
			heapSort.swapDown(self, 1)
		
		print '\n\nlist valid num 1--',maxnum,'\n des: ', self.m_array[:],'\n all size ', len(self.m_array)
	
if __name__ == '__main__':
	ar = []	
	while(len(ar) < 20): # random 20 interger 
		ar.append( random.randint(10,100) )
		
	print 'src ', ar, '\n len ', len(ar) 
	
	sorter = heapSort(ar)
	sorter.insert(200)
	sorter.delitem(3)
	sorter.sortData()	
	
	
	