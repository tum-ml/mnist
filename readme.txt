The aim of this project is to classify mnist handwritten data set using multiple machine learning algorithms and compare their results. This project is still under development.
	1) Knn : Achieved an accuray of 86.02% (using 60000 traning and 10000 testing samples)
	2) Neural network : Yet to be done
	3) logistic regression : Yet to be done
	4) gaussian processes : Yet to be done

Instructions for running the code knn/knn.ipynb:
	1. Open with Jupiter Notebook.
	2. (Optional) Readjust the values of Ntr (No of training samples <=60000) and Nte (No of test samples <= 10000) 	according to your requirements. Currently Ntr=2000 and Nte = 1000.
	3. (Optional) You may also adjust the value of k, but we have found k=15 to a reasonably optimal setting.
	4. Run the code.

Results:
	1. Accuracy is the indicator for the percentage of correctly classified test data points

data file names : 
	train-images.idx3-ubyte
	train-labels.idx1-ubyte
	t10k-images.idx3-ubyte
	t10k-labels.idx1-ubyte
	
Project Structure : 
	/testResults : This folder contains the result of test cases run by us.
	/research : some research papers that we have reffered.
	/lib : contains common code which can be used by different algos. e.g knnfeature extraction code, preprocessin of data, 	mnist data extraction etc. 
