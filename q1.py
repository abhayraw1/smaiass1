# SMAI Assignmnet #1 
#
# Author: Abhay Rawat
# Roll no: 20172082
# Dataset:https://researchweb.iiit.ac.in/ pinkesh.badjatiya/smai assignment1/q1 mnist train.csv
#
# ---------------------------------------------------------------------------------------------


import numpy as np;
import sys;

# Preprocessing Jobs:
def decision(x, w, bias):
	return (sum(x * w) + bias > 0);

def chopper(x):
	x = map(int, x.split(','));
	label = x.pop(0);
	return {'label': label, 'data' : np.array(x, dtype = np.float64)}

train_data = open('mnist_train.csv', 'r');
data_sets = map(chopper , train_data.readlines());
data_sets = data_sets[:int(len(data_sets))];
# print len(data_sets);
dim = data_sets[0]['data'].shape
# print dim
# sys.exit(0);
W = np.zeros(dim, dtype = np.float64);

# data_sets is now an array of dicts having two attributes 'label' and 'data'

# ---------------------------------------------------------------------------------------------

# 1. Single sample perceptron without margin
# print dim



# for i in data_sets:
# 	re = (sum(i['data'] * z) - 6.5) > 0;
# 	se = bool(i['label'])

# 	if(re != se):
# 		print 'shit', i;
# 	else:
# 		print (sum(i['data'] * z) - 6.5), se;

# sys.exit(0)

c = 0;
bias = 0;
flag = 1;
step_s = 0.5;
in_dev = True;

while flag:
	miss = 0;
	flag = 0;
	c += 1;
	if (not in_dev and c > 1000):
		break;
	# print c, bias;

	for i in data_sets:
		des = decision(i['data'], W, bias);
		label_b = bool(i['label'])
		if des == label_b:
			continue;
		elif des and not label_b:
			flag = 1
			bias -= step_s;
			W -= step_s * i['data'];
			miss += 1;
		elif not des and label_b:
			flag = 1
			bias += step_s;
			W += step_s * i['data'];
			miss += 1;
	print c, 1 - (float(miss)/float(len(data_sets)));

print W, bias;
train_data.close()
f = open('learn.csv', 'w');
w_str = ','.join(map(str, W));
f.write(w_str+'\n');
f.write(str(bias));
