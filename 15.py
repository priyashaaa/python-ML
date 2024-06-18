import csv
with open('message.txt', mode ='r')as file:
  csv_File = csv.reader(file)
for lines in csv_File:
	print(lines)
