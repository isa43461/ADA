def memo(m,n,A,B,mem):
	ans = None
	if (m,n) in mem: ans = mem[(m,n)]
	else:
		if(m == 0 or n == 0):
			ans = 0
		elif(m > 0 and n > 0):
			if(A[m-1] == B[n-1]):
				ans = 1 + memo(m-1,n-1,A,B,mem)
			else:
				ans = max(memo(m,n-1,A,B,mem), memo(m-1,n,A,B,mem))
		mem[(m,n)]=ans
	return ans

def tab(A,B,M,N):
	tabu = [[0 for _ in range(N+1)] for _ in range(M+1)]
	m,n = 1,1
	while(m!= M+1):
		if(n==N+1): m +=1; n = 1
		else: 
			if(m>0 and n>0):
		 		if(A[m-1] == B[n-1]):
		 			tabu[m][n] = 1 + tabu[m-1][n-1]
		 		else:
		 			tabu[m][n] = max(tabu[m][n-1],tabu[m-1][n])
		 		n+=1
	return tabu[M][N]

def tab2(A,B,M,N):
	tabu = [[0 for _ in range(M+1)] for _ in range(N+1)]
	m,n = 1,1
	while(n!= N+1):
		if(m==M+1): n +=1; m = 1
		else: 
			if(m>0 and n>0):
		 		if(A[m-1] == B[n-1]):
		 			tabu[n][m] = 1 + tabu[n-1][m-1]
		 		else:
		 			tabu[n][m] = max(tabu[n-1][m],tabu[n][m-1])
		 		m+=1
	return tabu[N][M]

def ls(A, lena):
  lis,lds = [ None for _ in range(lena) ],[ None for _ in range(lena) ]
  bestlis,bestlds = 0,0
  for n in range(lena):
    lis[n] = lds[n] = 1
    for i in range(n):
      if A[i]<=A[n] and lis[i]>=lis[n]: lis[n] = lis[i]+1
      if A[i]>=A[n] and lds[i]>=lds[n]: lds[n] = lds[i]+1
    bestlis,bestlds = max(bestlis, lis[n]),max(bestlds, lds[n])
  return (bestlds)

def main():
	A = [2,3,4,5,6]
	#a = [ 10, 3, 0, 8, 2, 4, 1, 6, 7, -2, 11 ]	
	B = [2,3,2,8,6]
	#mem = dict()
	#print(memo(len(A),len(B),A, B,mem))
	print(tab(A,B,len(A),len(B)))
	print(tab2(A,B,len(A),len(B)))
	#print(ls(a,len(a)))
main()
	
