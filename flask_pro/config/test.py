import numpy as np
from numpy.linalg import cholesky
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import math


plt.figure(figsize=(9, 16))
u = np.array([[0, 0]])  # 均值μ
sig = np.array([[1/2, 0], [0, 1/9]]) # 标准差δ
x = np.linspace(-3, 3, 4000)

R = cholesky(np.linalg.inv(sig))
s = np.dot(np.random.randn(500, 2), R) + u
#plt.subplot(144)
# 注意绘制的是散点图，而不是直方图
plt.plot(s[:, 0], s[:, 1], 'o')

y_sig = ((9-9/2*x*x))**0.5 #代入等密度面方程得到的解析式
plt.plot(x, y_sig, "r-", linewidth=2)
plt.plot(x, -y_sig, "r-", linewidth=2)
y_sig = ((9/2-9/2*x*x))**0.5
plt.plot(x, y_sig, "r-", linewidth=2)
plt.plot(x, -y_sig, "r-", linewidth=2)
y_sig = ((9/4-9/2*x*x))**0.5
plt.plot(x, y_sig, "r-", linewidth=2)
plt.plot(x, -y_sig, "r-", linewidth=2)
y_sig = ((18-9/2*x*x))**0.5
plt.plot(x, y_sig, "r-", linewidth=2)
plt.plot(x, -y_sig, "r-", linewidth=2)
y_sig = ((36-9/2*x*x))**0.5
plt.plot(x, y_sig, "r-", linewidth=2)
plt.plot(x, -y_sig, "r-", linewidth=2)
plt.savefig('./normal.png')
plt.show()
