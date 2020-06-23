from sys import stdin

def solve(n,p,r):
	ans = 0
	if(n == 1 and p == 1 and r == 1):
		ans = 1
	elif(p >= 1 and r >= 1 and n > 1):
		ans = solve(n-1,p,r)*(n-2) + solve(n-1,p,r-1) + solve(n-1,p-1,r)
	return ans

def main():
	cases = int(stdin.readline())
	while(cases != 0):
		A = [int(x) for x in stdin.readline().strip().split()]
		n = A[0]; p = A[1]; r = A[2]
		print(solve(n,p,r))
		cases-=1
main()