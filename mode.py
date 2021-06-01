import csv
import statistics

with open('SOCR-HeightWeight.csv',newline='') as f:
    reader= csv.reader(f)
    file_data = list(reader)

file_data.pop(0)
new_data=[]

for i in range(len(file_data)):
    n_num = file_data[i][2]
    new_data.append(n_num)

mode = statistics.mode(new_data)
print('Mode is '+str(mode)) 