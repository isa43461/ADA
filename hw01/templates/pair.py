from sys import stdin

def solve(point):
  ans = 0.0
  # ...
  return ans

def main():
  n = int(stdin.readline())
  while n!=0:
    point = list()
    for _ in range(n):
      tok = stdin.readline().split()
      point.append((float(tok[0]), float(tok[1])))
    print('{0:.4f}'.format(solve(point)))
    n = int(stdin.readline())

main()
