import math
def swap(n, i):
	if(n & (1<<i)):
		res = n - (1<<i)
	else:
		res = n + (1<<i)
	return res

def contar(n):
	print("contar", n)
	cnt = 0
	top = math.floor(math.log(n, 2)) + 1
	i = 0
	band = True
	while(i < top and band):
		if(n & (1<<i)):
			cnt += 1
		else:
			band = False
		i += 1
	return cnt


def f(n, seq):
	global seqRes, dict
	if(n == 0):
		if(res < len(seq)):
			seqRes = seq
	else:
		val = contar(n)
		print(n)
		if(n & 1 and (n-1) in dict and not dict[n-1] ):
			dict[n-1] = True
			f(n-1,seq + [1] )
		elif((n+1) in dict and not dict[n+1]):
			dict[n+1] = True
			f(n+1, seq + [1])
		f(swap(n, val), seq + [val])

seqRes = []
n = 2

dict = {}
print(f(n, []))



