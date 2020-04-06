from sys import stdin

def camping(n,k,dist,mid):
  i, j = 0,0
  acum = 0
  while(i!=n and j<=k):
    if(acum+dist[i] <= mid): 
      acum += dist[i]
      i+=1
    else:
      acum = 0
      j+=1 
  return j<=k

def solve(n, k, dist):
  low = 0; hi = sum(dist) 
  while(low+1!=hi):
    mid = ((hi+low)>>1)
    if(camping(n,k,dist,mid)): hi = mid
    else: low = mid 
  return hi

def main():
  N,K,dist = None,None,None
  line = stdin.readline()
  while len(line)!=0:
    N,K = map(int, line.split())
    n = N+1
    dist = [ int(stdin.readline()) for _ in range(n) ]
    print(solve(n, K, dist))
    line = stdin.readline()
main()
