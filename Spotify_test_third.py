import sys

lines = []
for line in sys.stdin:
    line = line.rstrip()
    linex = line.split(" ")
    lines.append(linex)
test_cases = int(lines[0][0])
y = 0
x = 0
lib = []
while (test_cases>0):
	y = y+x+1
	x = int(lines[y][2])
	
	lib.append(y)
	test_cases = test_cases - 1
lib.append(len(lines))

smell = []
for x in range (0,len(lib)-1):
	vote = lines[lib[x]+1 :lib[x+1]]
	smell.append(vote)



def add_zero (hip):
	for x in range(0,len(hip)):
	  hip[x].append(0)

def conflicts(smell):
	for x in range(0,len(smell)):
		
		smell[x][2] = 0
		for s in range(0, len(smell)):
			if smell[x][1] == smell[s][0]:
	
				smell[x][2] = smell[x][2]+1
			else:
				smell[x][2] = smell[x][2]+0
	return sorted(smell,key=lambda x: x[2],reverse=True)	
	  
def most (cuc):
	if len(cuc)>=1:
		while (cuc[0][2]>=1):
			cuc.remove(cuc[0])
			cuc = conflicts(cuc)
	return cuc

fish = []	
for x in range(0,len(smell)):
	  add_zero(smell[x])
	
for x in range(0,len(smell)):
	  fish.append(conflicts(smell[x]))
	 

ss = []
for x in range(0,len(fish)):
	  ss.append(most(fish[x]))
	  
for x in range(0,len(ss)):
	print len(ss[x])
	#print ss[x]	
	