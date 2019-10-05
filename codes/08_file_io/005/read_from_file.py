import os
file = open('test.txt', 'r')

# for i in range(1, 10):
#     print(file.read(5))

# print()

# for i in range(1, 10):
#     print(file.read(500))

for i in range(1, 10):
    print(file.read())

file.close()
