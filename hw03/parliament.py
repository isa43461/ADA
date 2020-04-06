from sys import stdin
import math

def solve(A,L,n):
	N = len(A); aux = None; value = 0
	for i in range(N):
		if(A[i] == n):
			aux = L[:i+1]
		if(A[i] > n):
			value = A[i] - n
			if(value == 1):
				aux = L[:i+2]
				aux.pop(0)
				penult = len(aux)-2
				aux.pop(penult)
			else:
				aux = L[:i+1]
				aux.remove(value)
			break
	return aux

def main():
	m = int(stdin.readline())
	L = [i for i in range(2,10000)]
	suma = 0; A = []
	for i in range(len(L)):
		suma += L[i]
		A.append(suma)
	for i in range(m):		
		space = stdin.readline().strip()
		n = int(stdin.readline())
		rp = solve(A,L,n)
		for i in range(len(rp)):
			print(rp[i],end = ' ')
		print("\n")
main()