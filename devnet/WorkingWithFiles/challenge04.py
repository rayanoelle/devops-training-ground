import csv
# CHALLENGE ONE
people = [

['Dan', 34, 'Bucharest'],

['Andrei',21, 'London'],

['Maria', 45, 'Paris']

]
with open('info.csv','w' , newline='')  as f:
    writer = csv.writer(f)
    writer.writerow(['name','age','city'])
    for row in people:
        writer.writerow(row)
with open('info.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
# CHALLENGE TWO
with open('info02.csv','w', newline='') as f:
    writer = csv.writer(f, delimiter=':')
    writer.writerow(['name','age','city'])
    for row in people:
        writer.writerow(row)