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
	def __init__(self, is_leaf = False, children = []):
		self.split = -1;
		self.attr_index = -1;
		self.children = children;
		self.is_leaf = is_leaf;
		self.value = None;

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

def get_best_split(data, classes):
	# indices = np.array(data.shape);
	splits = [[0 for i in is_discrete_attr] for j in xrange(len(data))];

	max_info_gain = 0;
	best_split = 0;
	split_index = -1;
	for i in xrange(len(is_discrete_attr)):
		print i
		x = extract_column(data, i);
		if not is_discrete_attr[i]:
			x = map(float, x);
		y = [j for (k,j) in sorted(zip(x, classes))]
		x.sort();
		# print zip(x,y)
		I1 = len([(k, l) for (k, l) in zip(x, y) if l == '1' ])
		I2 = len([(k, l) for (k, l) in zip(x, y) if l == '0' ])
		information = gini_index((I1, I2))
		for j in set(x):
			print j
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
				print max_info_gain, best_split, split_index
	
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

def split_data(data, classes, arr_index, split):
	z = zip(data, classes)
	if is_discrete_attr[arr_index]:
		total_data_l = [(x, y) for (x, y) in z if x[arr_index] == split]
		total_data_r = [(x, y) for (x, y) in z if x[arr_index] != split]
	else:
		total_data_l = [(x, y) for (x, y) in z if float(x[arr_index]) <= split]
		total_data_r = [(x, y) for (x, y) in z if float(x[arr_index]) > split]
	data_l = [x for (x, y) in total_data_l]
	class_l = [y for (x, y) in total_data_l]
	data_r = [x for (x, y) in total_data_r]
	class_r = [y for (x, y) in total_data_r]
	return data_l, class_l, data_r, class_r

def make_tree(data, classes, root):
	print len(data)
	if len(data) > 5 and classes.count('0') != len(data) and classes.count('1') != len(data):
		gain, root.split, root.attr_index = get_best_split(data, classes)
		print gain ,root.split, root.attr_index
		left_child = node()
		right_child = node()
		root.children = [left_child, right_child]
		data_l, class_l, data_r, class_r =  split_data(data, classes, root.attr_index, root.split)
		make_tree(data_l, class_l, left_child)
		make_tree(data_r, class_r, right_child)
	else:
		# print data
		root.is_leaf = True;
		root.value = max(classes, key = classes.count)

def validate(data, classes, root):
	print data[:5]
	print classes[:5]
	print 'validating'

if __name__ == '__main__':
	train_data_percent = .7;

	data = get_dataset('decision_tree_train.csv');
	data.pop(0);
	data = datatype(data);
	train_data = data[:int(len(data)* train_data_percent) ]
	train_class = extract_column(train_data, -4, True)
	validate_data = data[int(len(data) * train_data_percent):]
	validate_class = extract_column(validate_data, -4, True)
	
	is_discrete_attr = [not is_number(x) for x in train_data[0]];
	# print get_best_split(data, classes, is_discrete_attr)
	# print data;
	# print classes;
	root = node()
	# make_tree(train_data, train_classes, root)
	validate(validate_data, validate_class, root)
	# print get_best_split(data, classes)
	# a, b, c, d = split_data(data, classes, 6, 0.0)
	# print c, d
	# print get_best_split(a, b)
	
