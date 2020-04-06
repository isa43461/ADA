def lcs(A,B,m,n):
	if(m == 0 or n == 0):
		return 0
	elif(A[m-1] == B[n-1]):
		return 1 + lcs(A,B,m-1,n-1)
	else:
		return max(lcs(A,B,m-1,n), lcs(A,B,m,n-1))

def scs(A,B,m,n):
	if(m == 0):
		return n
	if(n == 0):
		return m
	elif(A[m-1] == B[n-1]):
		return 1 + scs(A,B,m-1,n-1)
	else:
		return 1 + min(scs(A,B,m-1,n),scs(A,B,m,n-1))

def main():
	A = "ABCDGH"
	B = "AEDFHR"
	print("lcs",lcs(A,B,len(A),len(B)))
	print("scs",scs(A,B,len(A),len(B)))
	#algoritmo hecho con referencia al Longest Increasing Subsequence p1 del libro
	#psdta: hice lo que pude :'v está en el archivo de intento
main()