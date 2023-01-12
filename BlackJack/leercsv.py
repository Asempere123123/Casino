import csv

with open('bj7.csv', newline='') as f:
    reader = csv.reader(f)
    your_list = list(reader)

print(your_list)