import sys
from svmutil import *
import math
import random

train_data = [];
train_data_X = [];
train_data_Y = [];
train_X = [];
train_Y = [];
val_X = [];
val_Y = [];



f = open(sys.argv[1], "r");
for line in f:
	line = line.strip().split();
	line.pop(0);
	line = map(float, line);
	train_data.append(line);
	train_data_X.append(line);
	# train_X.append(line);
f = open("../ML_final_project/truth_train.csv", "r");
data_num = 0;
for line in f:	
	line = line.strip().split(",");
	line = map(int, line);
	train_data[data_num].insert(0, line[1]);
	data_num += 1;
	train_data_Y.append(line[1]);
random.shuffle(train_data);
for i in range(data_num):
	tmp_data = train_data[i];
	if(i < data_num/5):
		val_Y.append(tmp_data[0]);
		tmp_data.pop(0);
		val_X.append(tmp_data);
	else:
		train_Y.append(tmp_data[0]);
		tmp_data.pop(0);
		train_X.append(tmp_data);

MAX_acc = 0;
MAX_C = -6;
MAX_Model = [];
for i in range(-6, 4, 2):
	print "logC = %d" % (i);
	param = '-t 2 -c ';
	param = param + str(10**i);
	model = svm_train(train_Y, train_X, param);
	# svm_save_model('model_file', model);
	p_labels, p_acc, p_vals = svm_predict(val_Y, val_X, model);
	if(MAX_acc < p_acc[0]):
		MAX_acc = p_acc[0];
		MAX_C = i;
		MAX_Model = model;

print "MAX_acc = %lf, MAX_C = %d" % (MAX_acc, MAX_C);
# svm_save_model('model_file', MAX_Model);
# MAX_C = 2;
param = '-t 0 -c ';
param = param + str(10**MAX_C);
model = svm_train(train_data_Y, train_data_X, param);
svm_save_model('model_file', model);
