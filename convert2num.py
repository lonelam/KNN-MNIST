import numpy as np
import struct
import matplotlib.pyplot as plt
import os

filename = '/Users/zhangmengxiao/Documents/codingfile/python/mnistConverter/train-labels-idx1-ubyte'
binfile = open(filename, 'rb')
buf = binfile.read()

index = 0
magic, numItem = struct.unpack_from('>II', buf, index)
index = index + struct.calcsize('>II')
myfile = open('./trainingSet/labels.txt', 'w')

for i in range(10000):
    label = struct.unpack_from('>B', buf, index)
    index = index + struct.calcsize('>B')
    oneline = 'The label of image ' + str(i) + ' is:' + str(label[0]) + '\n'
    myfile.write(oneline)


