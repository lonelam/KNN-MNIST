import knn
import matplotlib.pyplot as plt

sample, realLabel, predictLabel = knn.knn(10)
sample = sample.reshape(28, 28)
fig = plt.figure()
axes = fig.add_subplot(111)
plt.title('k = 10, the prediction is ' + predictLabel)
plt.imshow(sample)
plt.show()
