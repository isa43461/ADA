def maximo(cantidad,moneda, N):
	for i in range(N):
		if(cantidad < moneda[i]): return i-1
	return -1
def solve(moneda, A, cantidad, N):
	while(cantidad != 0):
		mx = maximo(cantidad, moneda,N)
		print(moneda[mx])
		cantidad -= moneda[mx]
		A.append(moneda[mx])
	return A
def main():
	A = []
	moneda = [1,5,10,25,100]
	N = len(moneda)
	cantidad = 34
	rp = solve(moneda, A, cantidad, N)
	print(rp)
main()

