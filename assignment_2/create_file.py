import os
import datetime

input_data = input('Please enter file contents?')

dir_name = datetime.date.today().strftime("%d-%m-%Y")

os.mkdir(dir_name)

dt_dir_path = os.path.join('.', dir_name)

file_path = os.path.join(dt_dir_path, 'input_data.txt')

with open(file_path,'w') as fd:
    fd.write(input_data)



