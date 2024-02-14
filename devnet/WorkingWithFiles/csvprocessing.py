import csv 
# READING CSV FILES (airtravel dataset)
with open('airtravel.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)
    year_1958 = dict()
    for row in reader:
        year_1958[row[0]] = row[1]
    max_1958 = max(year_1958.values())
    for key , value in year_1958.items():
        if value == max_1958:
            print(f'Busiest month in 1958 is {key} with {value} flights')
# # WRITING CSV FILES
with open('people.csv','a', newline='') as f:
    writer = csv.writer(f)
    csvdata = (5,'raya','tehran')
    writer.writerow(csvdata)
# # writing multiple rows
with open('numbers.csv','w' , newline='')  as f:
    writer = csv.writer(f)
    writer.writerow(['x', 'x**2', 'x**3' , 'x**3'])
    for x in range(1,101):
        writer.writerow([x,x**2,x**3,x**4])
# DIFFERENT DELIMITERS
with open('passwd.csv', 'r') as f:
    reader = csv.reader(f, delimiter=':', lineterminator='\n')
    for row in reader:
          print(row)
# CREATE YOUR OWN CSV DIALECT
csv.register_dialect('hashes', delimiter='#',quoting= csv.QUOTE_NONE, lineterminator='\n')
with open('items.csv', 'r') as f:
    reader = csv.reader(f,dialect='hashes')
    for row in reader:
        print(row)