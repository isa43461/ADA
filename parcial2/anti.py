from sys import stdin
def solve(A, n):
	aux = [A[0]]; i = 1
	while(i < n):
		l = len(aux)
		if(l%2 != 0):
			if(A[i-1] > A[i]):
				aux.append(A[i])
		else:
			if(A[i-1] < A[i]):
				aux.append(A[i])
		i+=1
	return aux

def main():
	cases = int(stdin.readline())
	while(cases != 0):
		A = [int(x) for x in stdin.readline().strip().split()]
		n = A.pop(0)
		rp = solve(A, n)
		print(len(rp))
		cases -= 1
main()