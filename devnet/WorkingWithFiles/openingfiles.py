#OPENING FILES
# f = open('conf.txt', 'r')
# content = f.read(5)
# print(content)
# print(f.tell())
# content = f.read(5)
# print(content)
# print(f.tell())
# f.seek(3)
# content = f.read(3)
# print(content)
# print(f.tell())
# # print(f.closed)
# f.close()
# print(f.closed)
with open('conf.txt' , 'r') as file:
    content = file.read()
    print(content)
    print(file.closed)
print(file.closed)