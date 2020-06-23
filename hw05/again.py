from sys import stdin
MAX = 10001
sieve = None
prime = None
divis = None

def build_sieve_opt():
	global sieve,prime,divis
	sieve = [ True for _ in range(MAX) ] ; sieve[0] = sieve[1] = False
	divis = [ None for _ in range(MAX) ]
	prime = [ 2 ] ; divis[1] = 1 ; divis[2] = 2
	for j in range(4, MAX, 2): sieve[j],divis[j] = False,2
	for i in range(3, MAX, 2):
		if sieve[i]:
			divis[i] = i
			prime.append(i)
			for j in range(i*i, MAX, i): sieve[j],divis[j] = False,i

def factorout(n):
	global divis, auxD
	while n!=1:
		d,cnt = divis[n],0
		while n%d==0: n,cnt = n//d,cnt+1
		ans[d] += cnt
		auxD[d] = ans[d]
	return ans

def factorout1(n):
	global divis, l
	ans = dict(); l = []
	while n!=1:
	  d,cnt = divis[n],0
	  while n%d==0: n,cnt = n//d,cnt+1
	  l.append(d)
	  ans[d] = cnt
	return ans

def main():
	global auxD,ans,l
	build_sieve_opt()
	auxD = dict()
	cont = 2; numero = 10000; ans = [0 for _ in range(numero)]; A = list()
	while(cont <= numero):
		z = factorout(cont)
		A.append(dict(auxD))
		cont += 1
	cases = int(stdin.readline())
	for i in range(cases):
		m, n = map(int,stdin.readline().strip().split())
		x = A[n-2]; N = len(x); band = False
		if m in x:
			print('Case {0}:'.format(i+1))
			print(x[m])
		else:
			rp = factorout1(m)
			ln = len(rp)
			aux = 0; vt = 5000
			for h in l:
				f = x.get(h)
				if(f != None):
					aux = x[h]//rp[h]
					vt = min(vt,aux)
				else:
					vt = 0
			if(vt == 0 or vt == 5000 or n == 1):
				print('Case {0}:'.format(i+1))
				print("Impossible to divide")
			else:
				print('Case {0}:'.format(i+1))
				print(vt)
main()