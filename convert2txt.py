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
imarray = []
myfile = open('./trainingSet/data.txt', 'w')

for i in range(5000):
    myfile.write(str(i) + '\n')
    im = struct.unpack_from('>784B', buf, index)
    index = index + struct.calcsize('>784B')
    str0 = ""
    for x in range(len(im)):
        lens = len(str(im[x]))
        if lens == 1:
            str0 = str0 + '   ' + str(im[x])
        if lens == 2:
            str0 = str0 + '  ' + str(im[x])
        if lens == 3:
            str0 = str0 + ' ' + str(im[x])
        if lens == 4:
            str0 = str0 + '' + str(im[x])
        if(x+1) % 28 == 0:
            str0 = str0 + '\n'
    myfile.write(str0+'\t')
    print(str0)
    print(i)

myfile.close()
    #im = im.reshape(28, 28)

    #fig = plt.figure()
    #plotwindow = fig.add_subplot(111)
    #plt.imshow(im, cmap='gray')
    #num = './pics/'+str(i)+'.png'
    #plt.savefig(num)
    #plt.close()

