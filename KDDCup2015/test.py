from svm import *
from svmutil import *
import sys;

f = open(sys.argv[1], "r");

ID = []
test_X = [];
test_Y = [];
for line in f:
	line = line.strip().split();
	ID.append(int(line[0]));
	line.pop(0);
	line = map(float, line);
	test_X.append(line);

test_Y = [0]*len(test_X);
model = svm_load_model('model_file');
p_labels, p_acc, p_vals = svm_predict(test_Y, test_X, model, '-q');

# print p_labels;
for i in range(len(test_X)):
	print "%d,%d" % (ID[i], p_labels[i]);