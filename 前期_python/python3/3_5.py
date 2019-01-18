import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

def mandelbrot(c, step):
	"""cについてstep回適用した差分方程式を計算する
	"""
	z = 0
	for s in range(step):
		z = z ** 2 + c
		if np.absolute(z) > 4.0:
			return step-1-s # zの絶対値(実数部)が４より大きくなるならば発散していくため計算回数に応じた数値を返す
	return 0 # step回計算しても４未満なら発散しないため0を返す

zspace = []
realspace = []
imagspace = []

for y in np.arange(-1.1,1.1,0.01): # -1.1から0.01刻みで1.1未満まで
	zdata = []
	reals = []
	imags = []

	for x in np.arange(-1.5,0.5,0.01): # -1.5から0.01刻みで0.5未満まで
		c = x + y * 1j
		m = mandelbrot(c, 100) # 差分方程式の計算
		zdata.append(m)
		reals.append(x)
		imags.append(y)

	zspace.append(zdata)
	realspace.append(reals)
	imagspace.append(imags)

plt.scatter(realspace, imagspace, c=zspace, marker=',', cmap='inferno', edgecolors='none') # 散布図の描画

plt.show() # グラフの表示
