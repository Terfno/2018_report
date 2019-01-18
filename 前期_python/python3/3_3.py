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

plt.scatter(xs,ys,s=1)
plt.xlabel('k')
plt.ylabel('xn')
plt.show()
