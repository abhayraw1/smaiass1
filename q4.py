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
	bow = {}
	for i in range(len(files)):
		print authors[i]
		for j in files[i]:
			words = get_words(j)
			for k in words:
				if not bow.has_key(k):
					bow[k] = {authors[i]: 1}
				else:
					if not bow[k].has_key(authors[i]):
						bow[k][authors[i]] = 1
					else:
						bow[k][authors[i]] += 1
	return bow

def get_author_word_usage(author, word, dict):
	if dict.has_key(author):
		return dict[author]
	return 0;

def gen_word_vector(dict, authors, word):
	l = []
	for i in authors:
		l.append(get_author_word_usage(i, word, dict))
	return l


def build_matrix(authors, bow):
	words = bow.keys()
	mat = np.matrix(np.zeros((len(authors), len(words))), dtype=np.float64)
	for i in xrange(len(words)):
		v = gen_word_vector(bow[words[i]], authors, words[i])
		mat[:, i] = np.matrix(v, dtype=np.float64).transpose()
	return mat, words

if __name__ == "__main__":
	authors, files = get_file_names(os.path.join(os.getcwd(), 'datasets/q4/train'))
	bow = build_dictionary(authors, files)
	print bow['the'].values()
	print len(bow)
	mat, words = build_matrix(authors, bow)
	a = ['the', 'be', 'to', 'of', 'and']
	x = [sum(bow[l].values()) for l in a]
	print x

	print mat[:, 0:5]
	
