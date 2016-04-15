#! /bin/env python
#author=changgy
#date=20160415

import os
import os.path


######################################################
def traverseDirByListdir(path):
    fileList=[]
    for f in os.listdir(path):
    	file = os.path.join(path,f)
    	if os.path.isfile(file):
    		fileList.append(file)
    	    
    return fileList
    

if __name__ == '__main__' :
	 
	#1. loop stl file list
	fileList = traverseDirByListdir(r'./')	
		
	#2. loop file
	for file in fileList:
		print file   