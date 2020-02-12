import csv

file = open('movies.csv', 'r')
reader = csv.reader(file)
for info in reader:
    print(info)