import knn
import matplotlib.pyplot as plt
import pylab

# fig = plt.figure()
# for i in range(1, 5):
#     sample, realLabel, predictLabel = knn.knn(30)
#     sample = sample.reshape(28, 28)
#     axes = fig.add_subplot(2, 2, i)
#     plt.title('the prediction is ' + predictLabel)
#     plt.imshow(sample)
#
# plt.show()


fig = plt.figure()
for i in range(1):
    sample, realLabel, predictLabel = knn.knn(10)
    sample = sample.reshape(28, 28)
    axes = fig.add_subplot(111)
    plt.title('the prediction result is ' + predictLabel)
    plt.imshow(sample)
    plt.show()