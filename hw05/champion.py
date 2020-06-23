from sys import stdin
import operator
MAX = 1000008
sieve = None
prime = None
divis = None

def binarySearch(v):
	global prime
	low = 0
	hi = len(prime)
	while(low+1 != hi):
		mid = (low+hi)//2
		if(prime[mid] > v):
			hi = mid
		else:
			low = mid
	return prime[low] == v,low

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

def solve(A,n):
	aux = []
	for i in range(1,n):
		acum = A[i] - A[i-1]
		aux.append(acum)
	oc = dict()
	for i in aux:
		if(oc.get(i) != None):
			oc[i] +=1
		else:
			oc[i] = 1
	l = sorted(oc.items(), key=operator.itemgetter(1), reverse=True)
	n = len(l); ans = 0
	if(n > 1):
		if(l[0][1] == l[1][1]):
			ans = 0
		else:
			ans = l[0][0]
	elif(n == 1):
		ans = l[0][0]
	return ans

def main():
	global prime
	cases = int(stdin.readline())
	build_sieve_opt()
	while(cases != 0):
		L,U = map(int,stdin.readline().strip().split())
		band0,lo = binarySearch(L)
		if(band0 == False):
			lo += 1
		band1,hi = binarySearch(U)
		A = prime[lo:hi+1] ; n = len(A)
		res = solve(A,n)
		if(res == 0):
			print("No jumping champion")
		else:
			print("The jumping champion is",res)
		cases -= 1
main()