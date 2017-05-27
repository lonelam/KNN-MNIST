#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import random
import operator

def knn(k):
    sample, label = _randomSample()
    sample = np.array(sample)
    trainingSet = _getTrainingSet()
    distlist = []
    for i in trainingSet:
        diff = np.subtract(sample, i[0])
        sq = diff ** 2
        sum = sq.sum(axis=0)
        distlist.append((sum, i[1]))

    sortedDis = sorted(distlist, key=lambda x:x[0], reverse=False)
    classcount = {}

    for i in range(k):
        voteLabel = sortedDis[i][1]
        classcount[voteLabel] = classcount.get(voteLabel, 0) + 1

    sortedClass = sorted(classcount.items(), key=operator.itemgetter(1), reverse=True)
    predictLabel = sortedClass[0][0].replace('\n', '')
    return sample, label, predictLabel
    #print('The prediction:' + sortedClass[0][0])
    #fig = plt.figure()
    #axes = fig.add_subplot(111)
    #title = 'k = ' + str(k) + ' and the prediction is ' + sortedClass[0][0]
    #plt.title(title)
    #toShow = sample.reshape(28, 28)
    #plt.imshow(toShow)
    #plt.show()
    #a = np.dtype(sample)
    #b = np.dtype(trainingSet[0][0])


def _getTrainingSet():
    myfile1 = open('./trainingSet/data.txt')
    myfile2 = open('./trainingSet/labels.txt')
    str1 = myfile1.read()
    str2 = myfile2.readlines()
    splited = str1.split('\t')
    splited.pop()

    for i in range(len(splited)):
        templist = splited[i].replace('\n', '').split(' ')[1:]
        noSpace = [int(element) for element in templist if element != '']

        splited[i] = np.array(noSpace).astype(np.float64)
        num = str2[i].split(':')[1]
        splited[i] = (splited[i], num)

    return splited

def _randomSample():
    list0 = []
    seed = random.randint(0, 5000)
    datafile = open('testSet/data.txt')
    str = datafile.read()
    splited = str.split('\t')
    splited = [ele.replace('\n', '') for ele in splited]

    list0.append(splited[seed])
    datafile.close()

    labelfile = open('testSet/labels.txt')
    str = labelfile.readlines()
    list0.append(str[seed])
    temp1 = str[seed].split(':')[1]
    temp2 = temp1.split('\n')[0]
    labelfile.close()

    sample2list = list0[0].split(' ')
    sample2list = [element for element in sample2list if element != '']

    return np.array(sample2list[1:]).astype(np.float64), temp2