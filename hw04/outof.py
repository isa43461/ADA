from sys import stdin

def solve(A,x,n):
	global band
	if(n == 1):
		if(A[0] == x):
			band = True
			return
	else:
		for i in range(n):
			v = A.pop(0)
			solve(A,x-v,len(A))
			solve(A,x+v,len(A))
			if(x % v == 0):
				solve(A,x//v,len(A))
			A.append(v)
def main():
	global band
	line = [int(x) for x in stdin.readline().strip().split()]
	while(line[0]!=0 and line[1]!=0 and line[2]!=0 and line[3]!=0 and line[4]!=0):
		band = False
		solve(line,23,len(line))
		if(band == True):
			print("Possible")
		else:
			print("Impossible")
		line = [int(x) for x in stdin.readline().strip().split()]
main()