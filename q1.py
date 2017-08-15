# SMAI Assignmnet #1 
#
# Author: Abhay Rawat
# Roll no: 20172082
# Dataset:https://researchweb.iiit.ac.in/ pinkesh.badjatiya/smai assignment1/q1 mnist train.csv
#
# ---------------------------------------------------------------------------------------------


import numpy as np;

# Preprocessing Jobs:
def class_(x):
	if(x):
		return x;
	return -1;


def chopper(x):
	x = map(int, x.split(','));
	return {'label':class_(x.pop(0)), 'data': np.matrix(x, dtype = np.float64)}

train_data = open('q1_mnist_train.csv', 'r');
data_sets = map(chopper , train_data.readlines());
dim = data_sets[0]['data'].shape
# data_sets is now an array of dicts having two attributes 'label' and 'data'

# ---------------------------------------------------------------------------------------------

# 1. Single sample perceptron without margin
# print dim
W = np.matrix(np.zeros(dim), dtype = np.float64).transpose();

itr = len(data_sets);
c = 1;
flag = 1;
print W;
while flag:
	print 'pass:      ', c;
	flag = 0;
	while itr:
		itr -= 1;
		current_label = data_sets[itr]['label']
		current_data = data_sets[itr]['data']
		res = np.float64(current_data * W);
		if((res * current_label) <= 0):
			W = W + (current_label * current_data.transpose());
			flag += 1;
	print 'changes in pass:     ', flag
	c = c + 1;
	itr = len(data_sets);

print W
print len(data_sets);