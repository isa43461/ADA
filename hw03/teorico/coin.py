# input: a[0..N) array of distinct positive integers, N>=0, and S
# output: number of ways that S can be obtained with an unlimited
#         amount of coins with denominations in a[0..N)
#
# O(NS) time and space solution using DP with tabulation (bottom-up)

def cc_tab(moneda, a):
  N = len(moneda)
  tab = [ [ None for s in range(a+1) ] for n in range(N+1) ]
  for s in range(a+1): tab[0][s] = 1 if s==0 else 0
  n,s = 1,0
  while n!=N+1:
    if s==a+1: n,s = n+1,0
    else:
      tab[n][s] = tab[n-1][s]
      if moneda[n-1]<=s: tab[n][s] += tab[n][s-moneda[n-1]]
      s += 1
  return tab[N][a]
def main():
  A = [1,2,3]
  n = 4
  print(cc_tab(A,n))
main()