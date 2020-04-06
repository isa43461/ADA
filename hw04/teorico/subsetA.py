lista = []
lista2 = []

def solve(A,x,i, ans):
	if(i == 0):
		if(x == 0):
			lista.append(list(ans))
	else:
		solve(A, x, i-1, ans)
		if(A[i-1]<= x):
			ans.append(A[i-1])
			solve(A, x-A[i-1], i-1, ans)
			ans.pop()

def solve2(A,N,x,i,ans):
	if(i == N):
		if(x == 0):
			lista2.append(list(ans))
	else:
		solve2(A,N,x,i+1,ans)
		if(A[i]<= x):
			ans.append(A[i])
			solve2(A,N,x-A[i],i+1,ans)
			ans.pop()

def main():
	global ans
	#A = [1,2,3,4,5,7]
	A = [1,2,4,5,2,1]
	x = 5; ans = list()
	solve(A,x,len(A), ans)
	solve2(A,len(A),x,0,ans)
	print(lista)
	print("El numero de arreglos que forman el numero",x,"es: ",len(lista))
	print(lista2)
	print("El numero de arreglos que forman el numero",x,"es: ",len(lista2))
main()