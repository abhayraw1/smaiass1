import numpy as np;
import cv2;
import sys;
from os import listdir
from os.path import isfile, join
mypaths = ["class 0", "class 1"];

file = open('validate.csv', 'w');

for x in xrange(len(mypaths)):
	mypath = mypaths[x];
	onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))];
	for i in onlyfiles:
		a = cv2.imread(join(mypath, i), 0);
		a = np.reshape(a, (a.size)).tolist();
		a.insert(0, x);
		a = ','.join(map(str, a));
		file.write(a + '\n');
file.close();
