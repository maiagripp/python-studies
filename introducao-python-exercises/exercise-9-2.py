import sys

with open(sys.argv[1], 'r') as file:
    for line in file.readlines()[int(sys.argv[2]) - 1 : int(sys.argv[3])]:
        print(line[:-1])

# print(sys.argv[1])
# print(sys.argv[2])
# print(sys.argv[3])