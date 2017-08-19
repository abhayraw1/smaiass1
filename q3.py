def get_dataset(filename):
	trainfile = open(filename, 'r');
	return trainfile.readlines();

def datatype(data):
	return [map(float, x.split(',')[:-2]) + x.strip('\n').split(',')[-2:] for x in data];

if __name__ == '__main__':
	data = get_dataset('decision_tree_train.csv');
	data.pop(0);
	print len(datatype(data))
	x =  datatype(data);
	for i in x:
		if len(i) != 10:
			print "fuck"
			break;


# class node:
	