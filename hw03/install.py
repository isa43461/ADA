from sys import stdin
import math

def intervalos(coord, d, n):
	A = []
	for i in range(n):
		formula = math.sqrt((d**2)-(coord[i][1]**2))
		A.append(((coord[i][0] - formula),(coord[i][0]+ formula)))
	return A

def solve(a,N):
	a.sort(key=lambda x : x[1]) 
	ans,n = 0,0
	while n!=N:
		best,n = n,n+1
		while n!=N and a[n][0]<a[best][1]:
			n += 1
		ans+=1
	return ans

def main():
	n,d = map(int, stdin.readline().strip().split())
	cases = 1
	while(n != 0 and d != 0):
		coord = list(); band = True
		for i in range(n):
			x, y = map(int, stdin.readline().strip().split())
			coord.append((x,y))
			if(y > d): 
				band = False
		if(band == True):
			A = intervalos(coord, d, n)
			rp = solve(A,n)
			print('Case {0}:'.format(cases),rp)
		else:
			print('Case {0}:'.format(cases),"-1")
		empty = stdin.readline().strip().split()
		cases +=1
		n,d = map(int, stdin.readline().strip().split())
main()