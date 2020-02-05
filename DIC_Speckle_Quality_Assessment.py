import random
import matplotlib.pyplot as plt
import numpy as np
from skimage import io


class Speckle(object):
    def __init__(self, img):
        self.__im = np.mat(img)
        if self.__im.dtype == np.float:  # 统一灰度值范围至8 bit 0-255
            self.__im = np.int64(255 * self.__im)
            # print(self.__im.dtype)

    def spec_qual(self, std='MeanIntensityGrad'):
        if std == 'MeanIntensityGrad':  # 平均灰度梯度
            gx, gy = np.gradient(self.__im)
            g_total = np.sqrt(np.multiply(gx, gx) + np.multiply(gy, gy))
            sizex, sizey = np.shape(g_total)
            return np.sum(g_total) / (sizex * sizey)

    def get_spec(self):
        return self.__im


if __name__ == '__main__':

    im = []
    for i in range(512):
        tmp = []
        for j in range(512):
            tmp.append(random.randint(0, 255))
        im.append(tmp)
    # plt.imshow(im, cmap='gray')
    # plt.show()

    random_spec = Speckle(im)  # random pic
    print('rand speckle MIG = %.5f' % random_spec.spec_qual())

    a = io.imread(r'C:\Users\Lenovo\Desktop\PyLearning\aoi.tif', as_gray=True)  # read in pics
    mySpeckle = Speckle(a)
    print('my speckle MIG   = %.5f' % mySpeckle.spec_qual())

    # plt.imshow(mySpeckle.get_spec(), cmap='gray')
    # plt.show()




