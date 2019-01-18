import matplotlib.pyplot as plt

xs=[]
ys=[]

for x in range(-10,11):
    y=x**2/10+2
    xs.append(x)
    ys.append(y)

plt.plot(xs,ys)

plt.xlim(-10,10)
plt.ylim(0,15)
plt.xticks(range(-10,11))
plt.yticks(range(0,16))
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.axhline(0,color='black',linewidth=0.5)
plt.axvline(0,color='black',linewidth=0.5)

plt.show()
