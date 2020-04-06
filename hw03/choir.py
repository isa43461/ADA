from sys import stdin

def solve(A,n):
	acum = 0
	for i in range(n):
		acum+= A[i]
	prom = acum//n; suma = 0
	for i in range(n):
		suma += abs(prom - A[i])
	ans = 0
	if(suma%2 != 0):
		ans = -1
	elif(acum%n != 0):
		ans = -1
	else:
		ans = (suma//2)+1
	return ans

def main():
	n = stdin.readline().strip()
	while(len(n)!=0):
		aux = stdin.readline().strip().split()
		A = []; N = int(n)
		for i in range(N):
			A.append(int(aux[i]))
		print(solve(A,N))
		n = stdin.readline().strip()
main()