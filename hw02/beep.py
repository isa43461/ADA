from sys import stdin
INF = float('inf')
#tsp 
def solve(v, A, vs,mx,beep,mem):
  ans = INF
  if (v,A) in mem:
    ans = mem[(v,A)]
  else:
    if A == (1<<beep) - 1:
      ans = mx[v][vs]
    else:
      for i in range(beep):
        if i != v and (A & (1<<i)) == 0:
          ans = min(ans, mx[v][i] + solve(i, (A | (1<<i)), vs,mx,beep,mem))
    mem[(v,A)] = ans
  return ans

def main():
  sc = int(stdin.readline().strip())
  for i in range(sc):
    aux = []; aux2 = [];mem = dict()
    mx = [[0 for _ in range(20)]for _ in range(20)]
    x,y = map(int, stdin.readline().strip().split())
    a,b = map(int, stdin.readline().strip().split())
    aux.append(a); aux2.append(b)
    beep = int(stdin.readline().strip()) 
    for i in range(beep):
      x1,y1 = map(int, stdin.readline().strip().split()) 
      aux.append(x1); aux2.append(y1)
    beep += 1 
    for i in range(beep):
      for j in range(beep):
        mx[i][j] = abs(aux[i]-aux[j]) +  abs(aux2[i]-aux2[j])
    print("The shortest path has length", solve(0,1,0,mx,beep,mem))
main()