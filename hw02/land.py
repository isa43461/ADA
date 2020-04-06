from sys import stdin
def solve(mx,row,col):
	aux = [0 for i in range(col)]
	q = []
	area = 0
	maxArea = 0
	for i in range(row):
		for j in range(col):
			if(mx[i][j] == 0):
				aux[j] = 0
			else:
				aux[j]+= 1
		#algoritmo para sacar el area en histogramas
		k = 0
		while(k<col):
			if(len(q) == 0 or aux[k] >= aux[q[-1]]): 
				q.append(k)
				k+=1
			else:
				top = q.pop()
				if(len(q)==0):
					area = (aux[top]*k)
				else:
					area = (aux[top]* (k - q[-1] - 1))
				if(maxArea<area): maxArea=area
		while(len(q)!=0):
		 	top = q.pop()
		 	if(len(q)==0):
		 		area = (aux[top] * k)
		 	else:
		 		area = (aux[top] * (k- q[-1] - 1))
	 		if(maxArea < area):
		 		maxArea = area
	return maxArea
def main():
	M,N = map(int, stdin.readline().strip().split())
	while (N!=0 and M!=0):
		A = []
		for i in range(M):
			l = stdin.readline().strip().split()
			for j in range(N):
				l[j] = int(l[j])
				if(l[j] == 0): l[j] = 1
				else: l[j] = 0 
			A.append(l)
		ans = solve(A,M,N)
		print(ans)
		M,N = map(int, stdin.readline().strip().split())
main()