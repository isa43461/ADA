def minimal_covering(L,H,l,h):
	ans,low,n = list(),L,0
	N = len(l)
	while low<H and n!=N:
		best,n = n,n+1
		while n!=N and l[n]<=low:
			if(h[n]>h[best]):
				best = n
			n+=1
		ans.append(best)
		low = h[best]
	return ans

def mic(L,H,a):
  a.sort()
  ans,low,n,N = list(),L,0,len(a)
  while low<H and n!=N:
    best,n = n,n+1
    while n!=N and a[n][0]<=low:
      if a[n][1]>a[best][1]:
        best = n
      n += 1
    ans.append(best)
    low = a[best][1]
  return ans


'''
p0: h[best] = (max i| 0<=i<n and l[best]<=low <= h[best])

p1: 0<=n<=N

p2: l<=low

p3: [l,low] contenido en la union [l[b[i]], h[b[i]]] for 0<=i<=len(b)
'''

def minimal_covering_with_failure(L,H,l,h):
	ans,low,n,ok = list(),L,0,True
	N = len(l)
	while ok and low<H and n!=N:
		ok = l[n]<=low and low <=h[n]
		best,n = n,n+1
		while ok and n!=N and l[n]<=low:
			if(h[n]>h[best]):
				best = n
			n+=1
		ans.append(best)
		low = h[best]
	ok = ok and low>=H
	if ok == False:
		ans = list()
	return ans

	