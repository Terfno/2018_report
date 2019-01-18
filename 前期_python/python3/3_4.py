import matplotlib.pyplot as plt
import numpy as np
import numpy.random as rnd

def logistic_map(x0,k,step):
    #初期値x 繁殖能力kでstep回適用したロジスティック写像を計算する

    x=x0
    for _ in range(0,step):
        x=k*(1.0-x)*x

    return x

ys=[]
xs=[]

for k in np.arange(2,4,0.0001):
    xs.append(k)

    xn=logistic_map(rnd.random(),k,1000)
    ys.append(xn)

plt.plot()
# plt.xlim(2.75,3.75)
# plt.xlim(2.75,3)
# plt.xlim(2.9,3)
# plt.xlim(2.99,3)
# plt.xlim(2.995,3)
plt.xlim(2.995,2.996)
# plt.ylim(0.4,0.8)
# plt.ylim(0.5,0.7)
# plt.ylim(0.650,0.675)
# plt.ylim(0.665,0.670)
# plt.ylim(0.650,0.667)
# plt.ylim(0.665,0.675)
plt.ylim(0.665,0.668)
plt.scatter(xs,ys,s=1)
plt.xlabel('k')
plt.ylabel('xn')
plt.show()



"""
result
(x,y)=(0.9955,0.66639)
"""
