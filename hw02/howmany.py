from sys import stdin

def solve(x,y,r,d,k,mem):
	global n
	key = (x,y,r,d)
	ans = None
	if key in mem: ans = mem[key]
	else:
		if(x == 2*n):
			if(y==0 and r==0 and d==0): ans = 1
			else: ans = 0
		else: 
			if(y == 0):	ans = solve(x+1,y+1,r,1,k,mem)
			else:
				if(d==0 or (d==1 and y!=k)):
					ans = solve(x+1,y+1,r,1,k,mem)+solve(x+1,y-1,r,0,k,mem)
				elif(d==1 and y==k and r==0): ans = solve(x+1,y+1,r,1,k,mem)
				elif(d==1 and y == k and r!=0):
					ans = solve(x+1,y+1,r,1,k,mem) + solve(x+1,y-1,r-1,0,k,mem)
		mem[key] = ans 
	return ans

def main():
	global n
	line = stdin.readline().strip().split()
	while(len(line)!=0):
		mem = dict()
		n = int(line[0]); r = int(line[1]) ;k = int(line[2])
		x, y, d = 0,0,None
		rs = solve(x,y,r,d,k,mem)
		print(rs)
		line = stdin.readline().strip().split()
main()