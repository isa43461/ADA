from sys import stdin

def solve(num, n):
  ans = None
  # ...
  return ans

def main():
  n = int(stdin.readline().strip())
  while n!=0:
    num = [ int(stdin.readline()) for _ in range(n) ]
    print(solve(num, n))
    n = int(stdin.readline().strip())
    

main()
