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

def add(bow, k, name):
	if not bow.has_key(k):
		bow[k] = {name: 1}
	else:
		if not bow[k].has_key(name):
			bow[k][name] = 1
		else:
			bow[k][name] += 1

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
# ----------------------------------------

def distance(v,u):
	v=v.transpose()
	u=u.transpose()
	v = np.array(v)
	u = np.array(u)
	normalise=np.sum(v)
	dist = 0
	for i in np.where(v!=0)[0]:
		print float(i)/v.shape[1]
		for j in np.where(u!=0)[0]:
			if i!=j:
				dist+=abs(v[i]*v[j] - u[i]*u[j])/(2*normalise)
	dist = np.sqrt(dist)
	dist += np.linalg.norm(v-u)/normalise
	return dist


def similarity(u,Authors,Mtrx):
	print Mtrx
	print u
	min_dist=distance(Mtrx[0,:],u)
	indx=0
	for i in range(len(Authors)):
		temp=distance(Mtrx[i,:],u)
		if temp<min_dist:
			indx=i
			min_dist=temp
	return indx


def Test(doc,dictionary, mat, authors):
	name="test_doc"
	temp_dictionary=dictionary.copy()

	doc=get_words(doc)
	for term in doc:
		if temp_dictionary.has_key(term):
			add(temp_dictionary,term,name)

	u=np.matrix(np.zeros((1,len(temp_dictionary))), dtype=np.float64)
	i=0
	for term in temp_dictionary.values():
		if term.has_key(name):
			u[0,i]=term[name]
		i=i+1

	ind=similarity(u, authors, mat)
	return ind
# -------------------------------------


if __name__ == "__main__":
	authors, files = get_file_names(os.path.join(os.getcwd(), 'datasets/q4/train'))
	bow = build_dictionary(authors, files)
	mat, words = build_matrix(authors, bow)
	tf = os.path.join(os.getcwd(), 'datasets/q4/test/thackerey/');
	print Test(os.path.join(tf, '1.txt'), bow, mat, authors)
	
