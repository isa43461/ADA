from sys import stdin
import math
INF = float("inf")
def distance(x,y):
	res = math.sqrt((x[0]-y[0])**2 + (x[1]-y[1])**2)
	return res

def solve(l, low, hi):
	if(hi-low == 1):
		res = distance(l[0], l[1])
		return res
	elif(hi-low == 0):
		return INF 
	else:
		mid = (hi+low)>>1
		izq = solve(l, low, mid)
		der = solve(l, mid, hi)
		a = min(izq, der)
		rs = 0
		i = mid + 1
		while(i <= hi):
			if(l[i][0]-l[mid+1][0] <= a):
				j = mid
				while(j >= low):
					if(l[i][0]-l[j][0] <= a):
						rs = distance(l[j], l[i])
						a = min(a,rs)
					else: 
						j = low
					j-=1
			else:
				i = hi
			i+=1
	
	return a
def main():
  n = int(stdin.readline())
  while n!=0:
    point = list()
    for _ in range(n):
      tok = stdin.readline().split()
      point.append((float(tok[0]), float(tok[1])))
    point.sort(key = lambda tup : tup[0])
    x = solve(point, 0, len(point)-1)
    if(x >=10000): print("INFINITY")
    else: print('{0:.4f}'.format(x))
    n = int(stdin.readline())

main()