from sys import stdin
import math
def mcd(a,b):
	ans = None
	if(b == 0):
		ans = a
	else:
		ans = mcd(b,a%b)
	return ans

def mcm(a,b):
	ans = (a // mcd(a,b))*b
	return ans

def divisores(line):
	A = []; l = int(math.sqrt(line))
	for i in range(1,l+1):
		if(line%i == 0):
			dc = line//i
			A.append(i)
			A.append(dc)
	A2 = []
	for i in A:
		if i not in A2:
			A2.append(i)
	return A2

def main():
	line = int(stdin.readline())
	while(line != 0):
		A = divisores(line);
		n = len(A); cont = 0
		for i in range(n):
			for j in range(i,n):
				if(mcm(A[i],A[j]) == line):
					cont += 1
		print(line,cont)
		line = int(stdin.readline())
main()