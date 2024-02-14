import csv
# FIRST WAY OF READING LINES INTO A LIST
with open('devices.txt' , 'r') as f:
    devices = []
    for line in f:
        properties = line.split(':')
        devices.append(properties)
    print(devices)
# SECOND WAY OF READING LINES INTO A LIST
with open('devices.txt', 'r') as f:
    reader = csv.reader(f, delimiter=':')
    devices = list()
    for row in reader:
        devices.append(row)
    print(devices)