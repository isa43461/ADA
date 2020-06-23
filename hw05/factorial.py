from sys import stdin

MAX = 1000008
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
	global divis, lista
	ans = 0
	while n!=1:
	  d,cnt = divis[n],0
	  while n%d==0: n,cnt = n//d,cnt+1
	  ans += cnt 
	return ans

def main():
	build_sieve_opt()
	cont = 2; numero = 10000; A = []; ans = 0
	while(cont <= numero):
		ans += factorout(cont)
		cont += 1
		A.append(ans)
	line = stdin.readline().strip().split()
	while(len(line)!= 0):
		n = int(line[0])-2
		print(A[n])
		line = stdin.readline().strip().split()
main()