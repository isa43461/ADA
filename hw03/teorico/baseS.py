from sys import stdin

def solve(A):
	cont = 0 ; i = 0 ; n = len(A)
	while(i < n):
		if(A[i] == '*'):
			cont += 1
			i+=4
		else:
			i+=1
	return cont

def main():
	A = stdin.readline().strip()
	rp = solve(A)
	print(rp)
main()