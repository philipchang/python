import math
import numpy as np
import pylab as pl
import random as rd

#计算平面两点的欧氏距离
def distance(a, b):
    return (a[0]- b[0]) ** 2 + (a[1] - b[1]) ** 2

#K均值算法
def k_means(x, y, k_count):
    count = len(x)      #点的个数
    #随机选择K个点
    k = rd.sample(range(count), k_count)
        
    k_point = [[x[i], [y[i]]] for i in k]   #保证有序
    k_point.sort()

    while True:
        km = [[] for i in range(k_count)]      #存储每个簇的索引
        #遍历所有点
        for i in range(count):
            cp = [x[i], y[i]]                   #当前点
            #计算cp点到所有质心的距离
            _sse = [distance(k_point[j], cp) for j in range(k_count)]
            #cp点到那个质心最近
            min_index = _sse.index(min(_sse))   
            #把cp点并入第i簇
            km[min_index].append(i)

        #更换质心
        k_new = []
        for i in range(k_count):
            _x = sum([x[j] for j in km[i]]) / len(km[i])
            _y = sum([y[j] for j in km[i]]) / len(km[i])
            k_new.append([_x, _y])

        k_new.sort()        #排序
        if (k_new != k_point):
            k_point = k_new
        else:
            return km


#计算SSE
def calc_sse(x, y, k_count):
    count = len(x)                              #点的个数
    k = rd.sample(range(count), k_count)        #随机选择K个点
    k_point = [[x[i], [y[i]]] for i in k]   
    k_point.sort()                              #保证有序

    #centroid
    sse = [[] for i in range(k_count)]
    while True:
        ka = [[] for i in range(k_count)]      #存储每个簇的索引
        sse = [[] for i in range(k_count)]
        #遍历所有点
        for i in range(count):
            cp = [x[i], y[i]]                   #当前点
            #计算cp点到所有质心的距离
            _sse = [distance(k_point[j], cp) for j in range(k_count)]
            #cp点到那个质心最近
            min_index = _sse.index(min(_sse))   
            #把cp点并入第i簇
            ka[min_index].append(i)
            sse[min_index].append(min(_sse))

        #更换质心
        k_new = []
        for i in range(k_count):
            _x = sum([x[j] for j in ka[i]]) / len(ka[i])
            _y = sum([y[j] for j in ka[i]]) / len(ka[i])
            k_new.append([_x, _y])

        k_new.sort()        #排序
        #更换质心
        if (k_new != k_point):
            k_point = k_new
        else:
            break

    s =0
    for i in range(k_count):
        s += sum(sse[i])
    return s


x, y = np.loadtxt('start.csv', delimiter=',', unpack=True)


'''
count_total = int(math.sqrt(len(x)))

k_t = []
for i in range(1, count_total + 1):
    s = calc_sse(x, y, i)
    k_t.append([s,i])

#k_t.sort(reverse=True)
#print k_t

ay = [item[0] for item in k_t]
ax = [item[1] for item in k_t]
pl.plot(ax, ay, 'r')
pl.grid()
pl.show()
'''

k_count = 6
km = k_means(x, y, k_count)


#使用Matplotlab画图

'''
	==========  ========
  character   color
  ==========  ========
  'b'         blue
  'g'         green
  'r'         red
  'c'         cyan
  'm'         magenta
  'y'         yellow
  'k'         black
  'w'         white
  ==========  ========
'''
colors = ['ob','og','or','oc','om','oy','ok'] # point style
for index in xrange(k_count):
	pl.plot([x[i] for i in km[index]], [y[i] for i in km[index]],  colors[index])

pl.grid()
pl.show()
