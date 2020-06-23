# O( (|V|+|E|) * log|V| ) usando min heap

from heapq import heappop, heappush

INF = float('inf')

def dijkstra(G, s):
  dist = [ INF for _ in G ]
  visited = [ False for _ in G ]
  dist[s] = 0
  heap = [(0, s)]
  while len(heap) != 0:
    d, u = heappop(heap)
    if visited[u] == False:
      for v, dv in G[u]:
        if d + dv < dist[v]: #Relajacion del vertice
          dist[v] = d + dv
          heappush(heap, (dist[v], v))
      visited[u] = True
  return dist

G = [[(1, 2), (2, 4)], [(2, 1), (3, 7)], [(4, 3)], [(5, 1)], [(3, 2), (5, 5)], []]

sol = dijkstra(G, 0)
for i in range(len(sol)):
    print("Node {0} | Dist {1}".format(i, sol[i]))

