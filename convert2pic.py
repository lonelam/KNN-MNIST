import numpy as np
import struct
import matplotlib.pyplot as plt
import os

filename = '/Users/zhangmengxiao/Documents/codingfile/python/mnistConverter/train-images-idx3-ubyte'
binfile = open(filename, 'rb')
buf = binfile.read()

index = 0
magic, numImages, numRows, numColumns = struct.unpack_from('>IIII', buf, index)
index = index + struct.calcsize('>IIII')


for i in range(10000):
    im = struct.unpack_from('>784B', buf, index)
    index = index + struct.calcsize('>784B')
    im = np.array(im)
    im = im.reshape(28, 28)

    fig = plt.figure()
    plotwindow = fig.add_subplot(111)
    plt.imshow(im, cmap='gray')
    num = './trainingSet/pics/'+str(i)+'.png'
    plt.savefig(num)
    plt.close()
    print(i)

