import os;
import numpy as np;
from os.path import basename, join

def get_file_names(path):
	l = os.walk(path)
	list_auth = []
	list_files = []
	for root, dirs, files in l:
		if len(files) > 0:
			list_auth.append(root.replace(path+'/', ''))
			auth_files = []
			for f in files:
				auth_files.append(root+"/"+f);
			list_files.append(auth_files)

	return list_auth, list_files

def get_words(file):
	return open(file, 'r').read().replace('\n', '').replace('<s> ', '').replace('<\s>', '').split(' ');

def build_dictionary(authors, files):
	dict = {}
	for i in range(len(files)):
		for j in files[i]:
			words = get_words(j)

if __name__ == "__main__":
	authors, files = get_file_names(os.path.join(os.getcwd(), 'datasets/q4/train'))
	build_dictionary(authors, files)
	
