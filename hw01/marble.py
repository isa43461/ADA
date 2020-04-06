from sys import stdin

def solve(A, num):
	#lower bound
	low, hi = 0, len(A)-1
	while(low<hi):
		mid = (low+hi)>>1
		if(A[mid] >= num): hi = mid 
		else: low = mid + 1
	return(A[low]==num, low)

def main():
	cont = 1
	N,Q = map(int, stdin.readline().strip().split())
	while(N != 0 and Q != 0):
		A = []
		for i in range(N):
			A.append(int(stdin.readline()))
		A.sort()
		print('CASE# {0}:'.format(cont))
		for i in range(Q):
			num = int(stdin.readline())
			band, indx = solve(A, num)
			if(band == False):
				print(num,"not found")
			else:
				print(num,"found at", indx+1)
		cont+=1
		N,Q = map(int, stdin.readline().strip().split())
main()