#READING FILES INTO LIST
#1. f.read().splitlines()
with open('conf.txt','r') as file:
    content = file.read().splitlines()
    print(content)
print(' '*20 +'-'*30)
#2. f.readLines()
with open('conf.txt','r') as f:
    content = f.readlines()
    print(content)
print(' '*20 +'-'*30)
with open('conf.txt', 'r') as f:
    print(f.readline( ))
    print(f.readline())
print(' '*20 +'-'*30)
#3. list(f)
with open('conf.txt', 'r') as f:
    content = list(f)
    print(content)
print(' '*20 +'-'*30)
#4.iterate over file
with open('conf.txt', 'r') as f:
    for line in f:
        print(line, end='')
print(' '*20 +'-'*30)