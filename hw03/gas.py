from sys import stdin

def solve(L,H,a):
	a.sort()
	ans,low,n,ok,N = list(),L,0,True,len(a)
	while ok and low<H and n!=N:
		ok = a[n][0]<=low
		best,n = n, n+1
		while ok and n!=N and a[n][0]<=low:
			if a[n][1]>a[best][1]:
				best = n
			n += 1
		ans.append(best)
		low = a[best][1]
	ok = ok and low>=H
	if ok == False:
		ans = list()
	return ans

def main():
	L,G = map(int, stdin.readline().strip().split())
	while(L!=0 and G!=0):
		A = []
		for i in range(G):
			x,r = map(int, stdin.readline().strip().split())
			A.append((x-r,r+x))
		rp = solve(0,L,A)
		if(len(rp) != 0):
			print(G - len(rp))
		else: 
			print("-1")
		L,G = map(int, stdin.readline().strip().split())
main()