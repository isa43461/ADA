from sys import stdin
def solve(g,l):
	if(l%g == 0):
		print(g,l)
	else:
		print(-1)

def main():
	cases = int(stdin.readline())
	while(cases != 0):
		G,L = map(int, stdin.readline().strip().split())
		solve(G,L)
		cases -= 1
main()