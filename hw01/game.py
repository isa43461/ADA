from sys import stdin
def solve(num):
  ans, cont = 0,0
  n = len(num)
  for i in range(n):
    ans += num[i]
    if(ans > 0): 
      if(ans > cont):
        cont = ans
    else:
      ans = 0
  return cont

def main():
  lista = stdin.readline().strip().split()
  while(len(lista)!=0):
    A = [int(x) for x in lista]
    rp = solve(A)
    print(rp)
    lista = stdin.readline().strip().split()
main()