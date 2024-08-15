import sys

with open(sys.argv[1], 'r') as odds, open(sys.argv[2], 'r') as even, open("output.txt", "w") as output:
    for line in odds.readlines():
        output.write(line)
    for line in even.readlines():
        output.write(line)