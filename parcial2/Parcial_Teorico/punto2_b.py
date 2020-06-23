def solve2(Arr):
	global n, lista, A
	if(Arr[-1] == n and len(Arr)== n-1 and Arr[0] == 1):
		lista.append(list(Arr))
	elif(Arr[-1] < n):
		x = Arr[-1]
		for i in Arr:
			if(i+x in A):
				Arr.append(i + x)
				solve2(Arr)
				Arr.pop()

def main():
	global n, lista, A
	lista = []
	num = [i for i in range(1, 10)]
	print(num)
	A = [i for i in range(20)]
	print(A)
	for x in num:
		n = x
		print("Número n:", n)
		solve2([1])
		print(len(lista),"|",lista)
		lista =[]
main()