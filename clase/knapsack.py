def knap(b,w,n,m,mem):
	ans = None
	if m in mem: ans = mem[m]
	else:
		if(n==0):
			ans = 0
		else:
			ans = knap(b,w,n-1,m,mem)
			if(w[n-1]<=m):
				ans = max(ans, knap(b,w,n-1,m-w[n-1],mem) + b[n-1])
		mem[m] = ans
	return ans

def knapTab(b,w,M):
	N = len(b)
	rp = [[0 for _ in range(M+1)] for _ in range(N+1)] 
	#for m in range(M+1): rp[0][m] = 0
	n,m =1,0
	while(n!= N+1):
		if(m==M+1):
			n,m = n+1,0
		else:
			rp[n][m] = rp[n-1][m]
			if(n!=0 and w[n-1]<=m):
				rp[n][m] = max(rp[n][m],b[n-1]+rp[n-1][m-w[n-1]])
			m+=1
	return rp[N][M]

def knapOpt(b,w,M):
	N = len(b)
	tab = [0 for _ in range(M+1)]
	n,m = 1,0
	while (n!=N+1):
		if(m==-1): n,m = n+1,M
		else:
			if(w[n-1]<=m): tab[m] = max(tab[m], b[n-1]+tab[m-w[n-1]])
			m-=1
	return tab[M]
def main():
	mem = dict()
	b = [3,7,5]
	w = [2,4,3]
	print(knap(b,w,len(b),4,mem))
	print(knapTab(b,w,4))
	print(knapOpt(b,w,4))
main()