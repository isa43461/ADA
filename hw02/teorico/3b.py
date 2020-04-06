from collections  import deque
def bfs(src, G, vis):
	q = deque()
	q.append(src)
	vis[src] = 1
	while(len(q)):
		u = q.popleft()
		for v in G[u]:
			if(vis[v] == 0):
				q.append(v)
			vis[v] = max(vis[v], 1+vis[u])
	return vis

def main():
	G = [[1],[2],[3,4],[],[5],[6],[]]
	vis = [0 for _ in range(len(G))]
	print(bfs(0,G,vis))
main()