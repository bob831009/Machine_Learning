import sys;

fp1 = open(sys.argv[1], "r");
fp2 = open(sys.argv[2], "r");

Total_line_num = sum(1 for line in open(sys.argv[1], "r"));

for i in range(Total_line_num):
	line1 = fp1.readline();
	line2 = fp2.readline();
	line1 = line1.strip();
	line2 = line2.strip().split(",", 1);
	# print line1;
	# print line2[1];
	print line1 + "," + line2[1];