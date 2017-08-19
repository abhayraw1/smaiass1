import numpy as np;
import sys;

def decision(x, w, bias):
	return (sum(x * w) + bias > 0);


def chopper(x):
	x = map(int, x.split(','));
	label = x.pop(0);
	return {'label': label, 'data' : np.array(x, dtype = np.float64)}


learn = open('learn.csv', 'r');
W = np.array(map(float, learn.readline().split(',')))
bias = float(learn.readline());
learn.close();
train_data = open('mnist_test.csv', 'r');

data_sets = map(chopper , train_data.readlines());
data_sets = data_sets[:int(len(data_sets))];

flag = 1;
c = 0;
in_dev = True;

while flag:
	miss = 0;
	flag = 0;
	if (not in_dev and c > 1000):
		break;
	# print c, bias;

	for i in data_sets:
		c+=1;
		des = decision(i['data'], W, bias);
		label_b = bool(i['label'])
		if des == label_b:
			print 'correct des', i['label'], c
			continue;
		elif des and not label_b:
			print 'shit', i
			miss += 1;
		elif not des and label_b:
			print 'shit', i
			miss += 1;

print 1 - float(miss)/float(len(data_sets));
print miss