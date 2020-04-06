from sys import stdin

def solve(A,n):
	global band
	aux = []
	if(n==0):
		band = True
		return
	else:
		if(n > 1):
			if(len(set(A)) == 1):
				band = True
				return
		for i in range(1,n):
			if(A[i-1] == A[i]):
				aux.append(i-1)
				if(i+1!=n):
					if(A[i] != A[i+1]):
						aux.append(i)
			else:
				if(len(aux)!=0):
					lista = A[:aux[0]]+A[aux[-1]+1:]
					solve(lista,len(lista))
					if(band == True):
						return
					aux = []
def main():
	global band
	cases = int(stdin.readline())
	while(cases != 0):
		band = False
		line = stdin.readline().strip()
		N = len(line)
		solve(line, N)
		if(band == True):
			print(1)
		else:
			print(0)
		cases-=1
main()