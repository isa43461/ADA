from sys import stdin
def solve(l): 
	ans = 0
	if(len(l) > 1):
		mid = len(l)>>1
		left = l[:mid]
		right = l[mid:]
		ans+=solve(left)
		ans+=solve(right)
		i,j,k = 0,0,0
		while(i < len(left) or j < len(right)):
			if(i < len(left) and j < len(right)):
				if(left[i] <= right[j]):
					l[k] = left[i]
					i+=1; k+=1
				else:
					l[k] = right[j]
					j+=1; k+=1
					ans += (len(left)-i)
			elif(i < len(left)):
					l[k] = left[i]
					i+=1; k+=1
			elif(j < len(right)):
					l[k] = right[j]
					j+=1; k+=1				
	return ans

def main():
	n = int(stdin.readline())
	while(n != 0):
		l = []
		for i in range(n):
			l.append(int(stdin.readline()))
		rp = solve(l)
		print(rp)
		n = int(stdin.readline())
main()