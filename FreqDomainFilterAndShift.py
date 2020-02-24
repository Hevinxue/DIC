# Basic staff
from skimage import io
import matplotlib.pyplot as plt
from matplotlib.colors import Normalize
import numpy as np

plt.figure()
a = io.imread(r'C:\Users\blabla', as_gray=True)  # read in pics
plt.subplot(3,2,1)
plt.imshow(a , cmap='gray',)


# Freq domain filter
a_fft = np.fft.fft2(a)
a_fft_raw = a_fft
a_fft = np.fft.fftshift(a_fft)
plt.subplot(3, 2, 2)
a_fft_module = abs(a_fft)
plt.imshow(a_fft_module , cmap='gray', norm=Normalize(0, 255))

filt = np.zeros_like(a_fft, dtype=float)  # filter
x, y = np.shape(a_fft)
filt[x//2-300 : x//2+301, y//2-300 : y//2+301] = 1
plt.subplot(3, 2, 3)
plt.imshow(filt , cmap='gray',)

plt.subplot(3, 2, 4)
plt.imshow(abs(a_fft*filt), cmap='gray', norm=Normalize(0, 255))

a_filted = np.fft.ifftshift(a_fft*filt)
a_filted = np.fft.ifft2(a_filted).real
# print(a_filted)
plt.subplot(3, 2, 5)
plt.imshow(a_filted, cmap='gray',)



# (Subpixel)Shift operated in freq domain
plt.figure()

row_shift = 400.0
col_shift = 300.0
# 原始方式构建频域的序列
# u = np.mat(np.fft.fftshift(np.arange(-x/2, x/2))).T  #行数，即列方向
# v = np.mat(np.fft.fftshift(np.arange(-y/2, y/2)))
# a_fft_submov = np.multiply(a_fft, np.exp(-2j*np.pi*((u/x)*row_shift + (v/y)*col_shift)))
'''↑ 相移exp(j*omega_x*deltaX + j*omega_y*deltaY); 使用加法运算符的broadcast，使e指数拓展为一个x*y矩阵.'''
# a_fft_submov = np.fft.ifftshift(a_fft_submov)


# 另一种方式使用np.fft.fftfreq()： 返回2j*pi*ft中的f，即f=k/N, k为采样窗口内的总周期数，N为采样窗口内的总采样点，即序列的某一维长度
uf = np.mat(np.fft.fftfreq(x, d=1.0)).T
vf = np.mat(np.fft.fftfreq(y, d=1.0))
a_fft_submov = np.multiply(a_fft, np.exp(-2j*np.pi*(uf*row_shift + vf*col_shift)))
a_fft_submov = np.fft.ifftshift(a_fft_submov)


a_submoved = np.abs(np.fft.ifft2(a_fft_submov))
plt.imshow(a_submoved, cmap='gray',)


plt.show()




























