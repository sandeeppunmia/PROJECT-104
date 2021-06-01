import csv
import statistics

with open('SOCR-HeightWeight.csv',newline='') as f:
    reader = csv.reader(f)
    file_data = list(reader)

#removing header
file_data.pop(0)
new_data = []
#checking the length of the file - no. of lines
for i in range(len(file_data)):
    n_num = file_data[i][2]
    new_data.append(float(n_num))

mean = statistics.mean(new_data)
print('Mean is '+ str(mean))

median = statistics.median(new_data)
print('Median is '+ str(median))

mode = statistics.mode(new_data)
print('Mode is '+ str(mode))