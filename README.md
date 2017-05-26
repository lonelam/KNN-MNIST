## mnistConverter and KNN

#### mnistConverter converts the datas from MNIST database of handwritten digits from bin to txt and png.

convert2txt.py converts the 't10k-images-idx3-ubyte' or 'train-images-idx3-ubyte' from bin to txt. It generates a series of 28*28 matrixes and write them to data.txt. Modify a few parameters to generate the quantity you want. It can be used to generate both training set and test set.

convert2pic.py converts the 't10k-images-idx3-ubyte' or 'train-images-idx3-ubyte' from bin to png. I just add a matplotlib module and use the matrixes to plot the figures and save them in ./trainSet/pic or ./testSet/pic. It can be used to generate both training set and test set.

convert2num.py converts the 't10k-labels-idx1-ubyte' or 'train-labels-idx1-ubyte' from bin to txt, which contains the labels of figures.

#### KNN finds the k nearest neighbors and then the test sample is assigned to the class most common among its k nearest neighbors.

The function knn requires one argument k to determine how many nearest neighbors you need. If you run the run.py, wait a few seconds and there it will show you a random test sample in png and print the predicted label.
