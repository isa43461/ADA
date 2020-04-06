from sys import stdin

def solve(n, k, dist):
  ans = None
  # ...
  return ans

def main():
  N,K,dist = None,None,None
  line = stdin.readline()
  while len(line)!=0:
    N,K = map(int, line.split())
    dist = [ int(stdin.readline()) for _ in range(N+1) ]
    print(solve(N, K, dist))
    line = stdin.readline()

main()
