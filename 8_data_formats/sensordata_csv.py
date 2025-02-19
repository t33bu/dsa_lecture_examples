import csv

file = open('data.csv')
reader = csv.reader(file,delimiter=',')
next(reader) # skip header
for row in reader:
    print(row[2],row[3])

print("")

file = open('data.csv')
dict_reader = csv.DictReader(file)
for row in dict_reader:
    print(row['value'],row['unit'])
    