import sys;
import re;
train_X = [];
flag = [];
line_size = 0;


f = open(sys.argv[1], "r");
line_num = 0;
for line in f:
	line = line.strip().split(",");
	if(line_num == 0):
		line = map(str, line);
		flag.extend(line);
		line_size = len(line);
	else:
		line = map(float, line);
		train_X.append(line);
	line_num += 1;


for i in range(len(train_X)):
	for j in range(len(train_X[0])):
		if(j == 0):
			print "%d" % (train_X[i][j]),;
		else:
			print "%d:%lf" %(j, train_X[i][j]),;
	print "";