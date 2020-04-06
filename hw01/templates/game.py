from sys import stdin

def solve(num, low, hi):
  r = None
  # ...
  return r

def main():
  inp = stdin
  for line in inp.readlines():
    num = [int(x) for x in line.strip().split()]
    print(max(solve(num, 0, len(num)), 0))
main()
