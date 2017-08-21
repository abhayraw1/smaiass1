import numpy as numpy
import q1

if __name__ == '__main__':
	train_data = open('q2_breast_cancer.train.csv', 'r');
	data_sets = map(chopper , train_data.readlines());
	train_data.close()
	data_sets = data_sets[:int(len(data_sets))];
	weight, bias = perceptron(data_sets, 0, step_s = 0.5, batch = True);

	validate('', weight, bias)
	f = open('learn3.csv', 'w');
	w_str = ','.join(map(str, weight));
	f.write(w_str+'\n');
	f.write(str(bias));
