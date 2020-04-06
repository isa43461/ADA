from sys import stdin
import math
def knap(A,m,n,num,mem):
	ans = None
	if (m,n) in mem: ans = mem[(m,n)]
	else:
		if(n == 0):
			if(m > 5000):
				ans = (num/(m))*100
			else:
				ans = 0
		else:
			ans = max(knap(A,m,n-1,num,mem), knap(A,A[n-1]+m,n-1,num,mem))
		mem[(m,n)] = ans
	return ans

def main():
	n,x = map(int, stdin.readline().strip().split())
	while(n!=0 and x!=0):
		l = []; st = 0; mem = dict()
		for i in range(n):
			num1,num2 = stdin.readline().split('.')
			num = int(num1)*100 + int(num2)
			if(i!=x-1):
				l.append(num)
			else:
				st = num
		if(st > 5000): print("100.00")
		else:
			print((knap(l,st,len(l),st,mem)))
		n,x = map(int, stdin.readline().strip().split())
main()