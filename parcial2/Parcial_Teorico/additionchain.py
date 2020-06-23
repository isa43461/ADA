def solve(A, n):
	global ans
	if(A[-1] == n):
		ans = min(ans, len(A))
	elif(A[-1] < n):
		x = A[-1]
		for i in A:
			A.append(i + x)
			solve(A,n)
			A.pop()

def main():
	global ans
	A = [1,2]; n = 11; ans = float("inf") 
	solve(A, n)
	if(n == 1):
		print(0)
	else:
		print(ans-1)
main()