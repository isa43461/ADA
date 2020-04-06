from sys import stdin

def solve(A):
	cont = 0 ; i = 0 ; n = len(A)
	while(i < n):
		if(A[i] == '.'):
			cont += 1
			i+=3
		else:
			i+=1
	return cont

def main():
	cases = int(stdin.readline())
	m = 1
	for i in range(cases):
		num = int(stdin.readline())
		A = stdin.readline().strip()
		rp = solve(A)
		print('Case {0}:'.format(m),rp)
		m +=1
main()