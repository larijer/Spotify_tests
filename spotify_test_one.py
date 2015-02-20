# assign my_num from stdin
import sys

line = raw_input()
my_num = int(line)
out = int(str(bin(my_num)[2:])[::-1],2)
print out
# print out to stdout
