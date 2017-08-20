import numpy as np
import sys;

def extract_column(data, index, delete = False):
	l = [];
	for i in data:
		if delete:
			l.append(i.pop(index));
		else:
			l.append(i[index]);
	return l;

def is_number(s):
	try:
		float(s)
		return True
	except ValueError:
		return False

def decision(value, split, discrete=False):
	if discrete:
		return value == split;
	return value <= split;


class node:
	def __init__(self, split, attr_index, is_leaf = False, children = []):
		self.split = split;
		self.attr_index = attr_index;
		self.children = children;
		self.is_leaf = is_leaf;

	def add_child(self, child):
		self.children.append(child)

	def make_leaf(self):
		self.is_leaf = True;


def get_dataset(filename):
	trainfile = open(filename, 'r');
	return trainfile.readlines();

def make_array(x):
	return x.strip('\n').split(',')

def datatype(data):
	return map(make_array, data);

def get_best_split(data, classes, is_discrete_attr):
	# indices = np.array(data.shape);
	splits = [[0 for i in is_discrete_attr] for j in xrange(len(data))];

	max_info_gain = 0;
	best_split = 0;
	split_index = -1;
	for i in xrange(len(is_discrete_attr)):
		x = extract_column(data, i);
		if not is_discrete_attr[i]:
			x = map(float, x);
		y = [j for (k,j) in sorted(zip(x, classes))]
		x.sort();
		# print zip(x,y)
		I1 = len([(k, l) for (k, l) in zip(x, y) if l == '1' ])
		I2 = len([(k, l) for (k, l) in zip(x, y) if l == '0' ])
		information = gini_index((I1, I2))
		for j in x:
			# print j
			pL1 = len([(k, l) for (k, l) in zip(x, y) if decision(k, j, is_discrete_attr[i]) and l == '1' ])
			pL2 = len([(k, l) for (k, l) in zip(x, y) if decision(k, j, is_discrete_attr[i]) and l == '0' ])
			pR1 = len([(k, l) for (k, l) in zip(x, y) if not decision(k, j, is_discrete_attr[i]) and l == '1' ])
 			pR2 = len([(k, l) for (k, l) in zip(x, y) if not decision(k, j, is_discrete_attr[i]) and l == '0' ])
 			curr_info_gain = info_gain((pL1, pL2),(pR1, pR2), information)
 			# print curr_info_gain, '<<<<<<<<<<,'
			if curr_info_gain > max_info_gain:
				max_info_gain = curr_info_gain
				best_split = j
				split_index = i
	
	return max_info_gain, best_split, split_index

def info_gain(left, right, I):
	total = float(sum(left) + sum(right))
	PL = sum(left)/total
	PR = sum(right)/total
	return I - PL * gini_index(left) - PR * gini_index(right)

def gini_index(P):
	if sum(P) == 0:
		return 0
	P = [float(x)/sum(P) for x in P]
	return 0.5 * (1 - sum([x**2 for x in P]))

def split_data(data, arr_index, split):
	if is_discrete_attr[arr_index]:
		return [x for x in data if x[arr_index] == split], [x for x in data if x[arr_index] != split]
	return [x for x in data if float(x[arr_index]) <= split], [x for x in data if float(x[arr_index]) > split] 

def make_tree(data, root):
	print 'tree is grwing'


if __name__ == '__main__':
	data = get_dataset('decision_tree_train.csv');
	data.pop(0);
	data = data[:100];
	data = datatype(data);
	classes = extract_column(data, -4);
	is_discrete_attr = [not is_number(x) for x in data[0]];
	gain, split, arr_index = get_best_split(data, classes, is_discrete_attr)
	root = node(split, arr_index)
	make_tree(data, root)
	print is_discrete_attr
	print split_data(data, 6, 0.0)[0]
	print '-----------------------'
	print split_data(data, 6, 0.0)[1]

