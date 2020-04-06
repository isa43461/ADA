from sys import stdin
from heap import heappush,heappop

def prim(G):
	ans = list()
	pq = list()
	for u,v,w in G[0]: heappush(pq,(w,u,v))
	visited = [False for _ in G] ; visited[0] = True
	while len(pq)!=0:
		w,u,v = heappop(pq)
		if (visited[v] == False): 
			visited[v] = True
			ans.append((u,v,w))
			for tu, tv, tw in G[v]: heappush(pq,(tw,tu,tv))
	return ans

def main():
	
main()