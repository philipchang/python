#! -*-coding:utf-8-*-

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pylab as pl
import xlwt
from scipy.cluster.vq import *

#t = np.arange(0.,4.,0.1)
#plt.plot(t,t, 'o', t,t+2, t,t**2, 'o')
#plt.bar(t,t**2)

#x = np.linspace(0,1)
#y = np.sin(4*np.pi*x)

#plt.subplot(221)
#np.exp(-5*x)
#at = np.arange(0,10)		
#plt.plot(at, at)

#plt.subplot(222)
#plt.axes([0.2,0.2, 0.5,0.5])
#t = np.arange(0,10)		
#plt.plot(t, t+2, color='red', linestyle='-', linewidth=3, label='Line1')


list1=[88,64,96,85]
list2=[92,99,95,94]
list3=[91,87,99,95]
list4 = [78,99,97,81]
list5=[88,78,98,84]
list6=[100,95,100,92]
tempdate = [list1, list2, list3, list4, list5, list6]
df = pd.DataFrame(tempdate, columns=['eng','alg','comp','math'])
df.to_csv(r"d:\df.csv")
df.to_excel(r'd:\df.xls',sheet_name='df')


df2 = pd.DataFrame.from_csv(r"d:\df.csv")
df2.to_csv(r"d:\df22.csv")

df.plot()
plt.show()

'''
plt.subplot(212)
t = np.arange(0,10)	
pl.plot(t, t)
plt.title('philip\'s python plot')
plt.xlabel('date')
plt.ylabel('value')
plt.legend(loc='bottom right')	
plt.show()
'''