# SMAI Assignmnet #1 
#
# Author:	Abhay Rawat
# Roll no:	20172082
# Dataset:	https://researchweb.iiit.ac.in/ pinkesh.badjatiya/smai assignment1/q1 mnist train.csv
#
# ---------------------------------------------------------------------------------------------


import numpy as np;
import sys;
from random import shuffle;


def decision(x, w, bias, margin):
	return (sum(x * w) + bias > margin);

def chopper(x):
	x = map(int, x.split(','));
	label = x.pop(0);
	return {'label': label, 'data' : np.array(x, dtype = np.float64)}

def update_vector(w, x, b, step_s, add_sub, margin relax):
	if relax:
		return update_vector_relaxed(w, x, b, step_s, add_sub, margin)
	w += (step_s * x) * add_sub;
	b += (step_s) * add_sub;
	return w, b

def update_vector_relaxed(w, x, b, step_s, add_sub, margin):
	addend = (step_s * (sum(x * w) + bias - margin)/ sum(x * x))
	w += addend * (x * add_sub);
	b += addend * bias
	return w, b


def update(des, label_b, w, x, b, step_s, flag, margin, relax):
	if des and not label_b:
		flag = 1
		w, b = update_vector(w, x, b, step_s, -1, margin, relax)
	elif not des and label_b:
		flag = 1
		w, b = update_vector(w, x, b, step_s, 1, margin, relax)
	return w, b, flag

def validate(file, W, bias, margin = 0):
	print 'validating'



def perceptron(data_sets, bias, step_s = 1, batch = False, margin = 0, epoch = None, relax = False):
	dim = data_sets[0]['data'].shape
	W = np.zeros(dim, dtype = np.float64)
	bias = 0
	flag = 1
	more_epoch = True;
	while flag and more_epoch:
		if bool(epoch):
			epoch -= 1;
			if epoch == 0:
				more_epoch = False
		batch_W = np.zeros(W.shape, dtype = np.float64)
		batch_bias = 0
		miss = 0;
		flag = 0;
		shuffle(data_sets)
		for i in data_sets:
			des = decision(i['data'], W, bias, margin);
			label_b = bool(i['label'])
			if des == label_b:
				continue;
			else:
				if not batch:
					W, bias, flag = update(des, label_b, W, i['data'], bias, step_s, flag, margin, relax)
				else:
					miss += 1
					batch_W, batch_bias, flag = update(des, label_b, batch_W, i['data'], batch_bias, step_s, margin, flag, relax)
		print 1- float(miss)/len(data_sets)
		if batch:
			W += batch_W
			bias += batch_bias
	return W, bias

if __name__ == '__main__':
	train_data = open('mnist_train.csv', 'r');
	data_sets = map(chopper , train_data.readlines());
	train_data.close()
	data_sets = data_sets[:int(len(data_sets))];
	weight, bias = perceptron(data_sets, 0, step_s = 0.5, batch = True);

	validate('', weight, bias)
	f = open('learn3.csv', 'w');
	w_str = ','.join(map(str, weight));
	f.write(w_str+'\n');
	f.write(str(bias));
