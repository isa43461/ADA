def safe(A,v,color,c):
	ans = True
	for i in range(len(A)):
		if(A[v][i] == 1 and color[i]==c):
			ans = False
	return ans

def solve(A,m,color,v,al):
	if v == len(A[0]):
		al.append(list(color))
	else:
		for c in range(1,m+1):
			if safe(A,v,color,c):
				color[v] = c
				solve(A,m,color,v+1,al)
def main():
	al = []
	A = [[0,1,1,1],[1,0,1,0],[1,1,0,1],[1,0,1,0]]
	v = len(A)
	color = [None for _ in range(v)]
	m = 4
	solve(A,m,color,0,al)
	print(al)
main()
