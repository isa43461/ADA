from sys import stdin

def solve(n, k, memo):
	assert 0 <= k <= n
	ans,key = None,(n, k)
	if key in memo: ans = memo[key]
	else:
		if k==0 or k==n: ans = 1
		else:
			if n<(k<<1): k = n-k
			ans = solve(n-1, k-1,  memo) + solve(n-1, k, memo)
		memo[key] = ans
	return ans

def main():
	k = stdin.readline().strip().split()
	mem = dict()
	while(len(k)!= 0):
		for i in range(int(k[0])):
			l = stdin.readline().strip().split()
			N, T, P = int(l[0]), int(l[1]), int(l[2])
			if(P*N<= T):
				res = solve(T-P*N + N-1,N-1,mem)
				print(res)
			else: print(0)
		k = stdin.readline().strip().split()
main()