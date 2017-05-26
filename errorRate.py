import knn
import matplotlib.pyplot as plt

num = 0.0
kList = [1, 2, 5, 10, 20]
rateList = []

for x in kList:
    num = 0.0
    for i in range(50):
        sample, realLabel, predictLabel = knn.knn(x)
        print(realLabel)
        print(predictLabel)
        if realLabel == predictLabel:
            num += 1
    accuracy = num/50
    rateList.append(accuracy)

fig = plt.figure()
axes = fig.add_subplot(111)
plt.plot(kList, rateList, linestyle='dashed', marker='o')
plt.show()

