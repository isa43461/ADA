def positiveInterval(A,N): 
	acum = 0; tmp = 0; i = 1
	while(i <= N):
		if(acum == 0 and A[i-1] < 0):
			i+=1
		else:
			if(acum+A[i-1]<0):
				acum+=A[i-1]
				if(acum+A[i]<0):
					acum = 0
					tmp +=1
			else:
				acum += A[i-1]
		i+=1
	if(acum > 0):
		tmp +=1
	return tmp 

def main():
	A = [3,-5,7,-4,1,-8,3,-7,5,-9,5,-2,4]
	A2 = [-3,-5,-7,-4,-1,-8,-3,-7,-5,-9,-5,2,4]
	A3 = [-2,-3,-5]
	A4 = [1,2,3,5]
	N = len(A); N2 = len(A2); N3 = len(A3); N4 = len(A4)
	print(positiveInterval(A, N))
	print(positiveInterval(A2, N2))
	print(positiveInterval(A3, N3))
	print(positiveInterval(A4, N4))
main()