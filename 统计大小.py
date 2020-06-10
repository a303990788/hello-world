import os

all_files = os.listdir(path='F:\PYTHON')
file_dict = dict()

for each_file in all_files:
    if os.path.isfile(each_file):
        file_size = os.path.getsize(each_file)
        file_dict[each_file] = file_size


for each_dict in file_dict:
    print('%s的大小是%d byes' % (each_dict,file_dict[each_dict]))
