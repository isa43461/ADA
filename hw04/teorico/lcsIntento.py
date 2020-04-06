def aux(A,B,m,n):
    best = 0
    while n != 0:
        if A[m-1] == B[n-1]:
            best = 1 + max(best,lcs(A,B,m-1,n-1))
        n-=1
    return best

def lcs(A,B,m,n):
    best = 0
    while m != 0:
        best = max(best, aux(A,B,m,n))
        m-=1
    return best

def main():
	A = 'ABCDGH'
	B = 'AEDFHR'
	A1 = 'AGGTAB'
	B1 = 'GXTXAYB'
	print(lcs(A,B,len(A),len(B)))
	print(lcs(A1,B1,len(A1),len(B1)))
main()