import numpy;
import cv2;


train_data = open('q1_mnist_train.csv', 'r');
c = 0;
for i in train_data.readlines():
	arr = map(int, i.split(','));
	label = arr.pop(0);
	c += label;
	# img = numpy.array(arr).reshape(28,28);
	# name = label + '__' + str(c)+'.png';
	# c = c + 1;
	# cv2.imwrite(name, img);
	# if(c == 1000):
		# break;
print c;
print len(train_data.readlines());

# img = numpy.matrix(numpy.ones([500,500,1])).reshape(500,500,1)
# # img[:,:,0] = numpy.ones([500,500])*64/255.0
