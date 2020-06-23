from heapq import heappop,heappush

ORDA = ord('A')

class node(object):
  def __init__(self, lab=None, l=None, r=None, f=None):
    self.lab = lab
    self.l = l
    self.r = r
    self.f = f

def traverse_tree(t, ans, path):
  if t.l==None and t.r==None: ans[t.lab] = ''.join(path)
  else:
    path.append('0') ; traverse_tree(t.l, ans, path) ; path.pop()
    path.append('1') ; traverse_tree(t.r, ans, path) ; path.pop()

def build_codes(s):
  ans = dict()
  freq = [ 0 for _ in range(26) ]
  for c in s: freq[ord(c)-ORDA] += 1
  h,t = list(),dict()
  for i in range(len(freq)):
    if freq[i]!=0:
      heappush(h, (freq[i], chr(i+ORDA)))
      t[chr(i+ORDA)] = node(chr(i+ORDA), None, None, freq[i])
  while len(h)>=2:
    f1,s1 = heappop(h) ; t1 = t[s1]
    f2,s2 = heappop(h) ; t2 = t[s2]
    f3,s3 = f1+f2,s1+s2
    heappush(h, (f3, s3))
    t[s3] = node(s3, t1, t2, f3)
  traverse_tree(t[h[0][1]], ans, list())
  return ans

print(build_codes('ASDLASJLDJQZZWLDQWODIJASLDK'))
