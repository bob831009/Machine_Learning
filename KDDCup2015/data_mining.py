import sys;

ID_data = [];
total_log_num = 0;
log_num = dict();
tmp_ID = -1;
Total_Event = ['server_nagivate', 'server_access', 'server_problem', 'browser_access', 'browser_problem', 'browser_page_close', 'browser_video', 'server_discussion', 'server_wiki'];

f = open(sys.argv[1], "r");
line_num = 0;
Total_line_num = sum(1 for line in open(sys.argv[1], "r"));
# print Total_line_num;
for line in f:
	line_num += 1;
	if(line_num == 1):
		continue;
	line = line.strip().split(",");
	if(tmp_ID != int(line[0])):
		if(tmp_ID != -1):
			tmp_data = [];
			tmp_data.append(tmp_ID);
			tmp_data.append(total_log_num);
			for event in Total_Event:
				tmp_data.append(log_num[event]);
			ID_data.append(tmp_data);

		tmp_ID = int(line[0]);
		for event in Total_Event:
			log_num[event] = 0;
		total_log_num = 0;
	else:
		event = line[2]+'_'+line[3];
		if(event not in log_num):
			print "ERROR: event not in log_num";
		log_num[event] += 1;
		total_log_num += 1;

	if(line_num == Total_line_num and tmp_ID != -1):
		tmp_data = [];
		tmp_data.append(tmp_ID);
		tmp_data.append(total_log_num);
		for event in Total_Event:
			tmp_data.append(log_num[event]);
		ID_data.append(tmp_data);

f = open(sys.argv[2], "r");
line_num = 0;
for line in f:
	line = line.strip().split(",");
	# print line[15:];
	if(line_num == 0):
		Total_Event.extend(line[15:]);
	else:
		line = map(int, line);
		ID_data[line_num - 1].extend(line[15:]);
	line_num += 1;
# print ID_data;
sys.stdout.write("enrollment_id,Total_log_num");
for event in Total_Event:
	sys.stdout.write(","+event);
print "";

for elem in ID_data:
	sys.stdout.write(str(elem[0]));
	for i in range(1, len(elem)):
		sys.stdout.write(","+str(elem[i]));
	print "";
