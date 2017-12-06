import numpy as np
from numpy import linalg as LA

def knn_x(data, x, k):
	n,m = data.shape

	x_data = np.tile(x,(n,1))
	dist_matrix = LA.norm((x_data - data),axis=1)

	neighbors_indexes = np.argsort(dist_matrix)[:k]
	return neighbors_indexes

def knn_clf_x(neighbors, true_labels):
	votes = []
	for idx in neighbors:
		votes.append(true_labels[idx])
	votes = np.array(votes,dtype ='int')
	return np.argmax(np.bincount(votes))

def knn_algorithm(train_data,train_labels,test_data,k):
	preds = []
	for x in test_data:
		neighbors = knn_x(train_data,x,k)
		preds.append(knn_clf_x(neighbors,train_labels))
	return np.array(preds)

def calc_error(true_labels,pred_labels):
	assert true_labels.size == pred_labels.size, "Vectors not equal size"
	n = true_labels.size
	miscount = 0.0
	for i in xrange(n):
		if true_labels[i] != pred_labels[i]:
			miscount += 1.0
	return  (miscount/n)

def main():
	f = open('output.txt','w')
	train = np.genfromtxt('data/train_data.txt')
	test = np.genfromtxt('data/test_data.txt')
	val = np.genfromtxt('data/val_data.txt')


	n_feat = train[0].size
	train_data = train[:,:-1]
	train_labels = train[:,n_feat-1]
	test_data = test[:,:-1]
	test_labels = test[:,n_feat-1]
	val_data = val[:,:-1]
	val_labels = val[:,n_feat-1]

	k_neighbors = [1,3,5,11,16,21]
	for k in k_neighbors:
		preds_train = knn_algorithm(train_data,train_labels,train_data,k)
		preds_val = knn_algorithm(train_data,train_labels,val_data,k)
		preds_test = knn_algorithm(train_data,train_labels,test_data,k)
		f.write("%s-neighbors: \n" % k)
		f.write("Training error: %s \n" % (calc_error(train_labels,preds_train)))
		f.write("Validation error: %s \n" % (calc_error(val_labels,preds_val)))
		f.write("Test error: %s \n" % (calc_error(test_labels,preds_test)))
		f.write("\n")

if __name__ == '__main__':
main()