import numpy
import cv2;
from numpy import linalg;
import sys, os;

# s = open('data0', 'rb');
# out = open('train.csv', 'r');
# # x = s.read(16);
# for i in range(1000):
# 	images = [];
# 	for j in range(28*28):
# 		images.append(ord(s.read(1)))
# 	# img = np.reshape(np.array(images),(28,28))
# 	images.insert(0, 0);
# 	print len(images)
# 	img = ','.join(map(str, images));
# 	# print img;
# 	out.write(img+'\n');
# 	# break;
# 	# cv2.imwrite('0_'+ str(i) +'.png', img);
# s.close();
# sys.exit(0);



# def chopper(x):
# 	x = map(int, x.split(','));
# 	label = x.pop(0);
# 	return {'label': label, 'data' : np.array(x, dtype = np.float64)}


# train_data = open('q1_mnist_train.csv', 'r');
# data_sets = map(chopper , train_data.readlines());
# dim = data_sets[0]['data'].transpose().shape;
# W = np.zeros(dim, dtype = np.float64);

# Y = np.matrix([x['label'] for x in data_sets]).transpose();
# X = np.matrix([x['data'] for x in data_sets]);

# invx = linalg.pinv(X)
# print Y[:10,:];
train_data = open('q1_mnist_train.csv', 'r');
c = 0;
for i in train_data.readlines():
	arr = map(int, i.split(','));
	label = arr.pop(0);
	c += label;
	img = numpy.array(arr).reshape(28,28);
	name = str(label) + '__' + str(c)+'.png';
	c = c + 1;
	cv2.imwrite(name, img);
	if(c == 1000):
		break;
print c;
print len(train_data.readlines());
img = numpy.matrix(numpy.ones([500,500,1])).reshape(500,500,1)
# img[:,:,0] = numpy.ones([500,500])*64/255.0
