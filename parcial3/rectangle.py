def kadane(A,n,mem):
	ans = None 	#algoritmo visto en clase
	if n in mem: ans = mem[n]
	else:
		if(n == 0):
			ans = A[0]
		else:
			ans = max(kadane(A,n-1,mem) + A[n-1], A[n-1])
		mem[n] = ans
	return ans
def solve(A,row,col):
	INF = -float('inf')
	for i in range(col):
		aux = [0 for x in range(row)]
		for j in range(i,col):
			for k in range(row):
				aux[k] += A[k][j]
			suma = kadane(aux,row,dict())
			INF = max(suma,INF)
	return INF

def main():
	A = [[1, 2, -1, -4, -20],[-8, -3, 4, 2, 1],[3, 8, 10, 1, 3],[-4, -1, 1, 7, -6]]
	A1 = [[2,1,-3,-4,-5],[0,6,3,4,1],[2,-2,-1,4,-5],[-3,3,1,0,3]]
	col = len(A[0])
	row = len(A)
	col1 = len(A1[0])
	row1 = len(A1)
	print(solve(A,row,col))
	print(solve(A1,row1,col1))
main()