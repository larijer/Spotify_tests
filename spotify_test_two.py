#Jered Karr
#Code return most popular "song" indenpendent of song location of album
# two sample inputs are sample input 1 and sample in 2


# assign my_num from stdin
import sys

lines = []
for line in sys.stdin:
    line = line.rstrip()
    linex = line.split(" ")
    lines.append(linex)
    # print line
    

song_count = int(lines[0][0])+1
numb_return = int(lines[0][1])


for x in range(1, song_count):
    q = int(lines[x][0]) * x
    lines[x].append(q)


lip = sorted(lines[1:song_count], key=lambda x: x[2],reverse=True)

for x in range(0,numb_return):
    print lip[x][1]
    #print lip[x]







# print numb_return
# print out to stdout