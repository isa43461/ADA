# O(|V|^2) sin minheap (matriz de adyacencia)
# O(|E|*log|V|) con minheap (lista de adyacencia)

from heapq import heappush, heappop

############Codigo para grafo como lista de arcos##############
def prim(G):
    ans, pq = list(), list()
    u,v,w =  G[0]
    heappush(pq, (w, u, v))
    visited = [False for _ in G]
    visited[0] = True
    while len(pq) != 0:
        w, u, v = heappop(pq)
        if visited[v] == False:
            visited[v] = True
            ans.append((u, v, w))
            for tu, tv, tw in G[v]:
                heappush(pq, (tw, tu, tv))

G = [ (0, 1, 5),
      (0, 5, 4),
      (1, 2, 1),
      (1, 3, 8),
      (1, 7, 5),
      (2, 4, 4),
      (2, 5, 2),
      (2, 6, 1),
      (3, 4, 4),
      (5, 6, 3),
      (5, 7, 2),
      (6, 8, 6) ]



############Codigo para grafo como matriz de adyacencia##############

def printMST(self, parent): 
        print "Edge \tWeight"
        for i in range(1, self.V): 
            print parent[i], "-", i, "\t", self.graph[i][ parent[i] ] 

def minKey(self, key, mstSet): 
  
        # Initilaize min value 
        min = sys.maxint 
  
        for v in range(self.V): 
            if key[v] < min and mstSet[v] == False: 
                min = key[v] 
                min_index = v 
  
        return min_index 
  
    # Function to construct and print MST for a graph  
    # represented using adjacency matrix representation 
    def primMST(self): 
  
        # Key values used to pick minimum weight edge in cut 
        key = [sys.maxint] * self.V 
        parent = [None] * self.V # Array to store constructed MST 
        # Make key 0 so that this vertex is picked as first vertex 
        key[0] = 0 
        mstSet = [False] * self.V 
  
        parent[0] = -1 # First node is always the root of 
  
        for cout in range(self.V): 
  
            # Pick the minimum distance vertex from  
            # the set of vertices not yet processed.  
            # u is always equal to src in first iteration 
            u = self.minKey(key, mstSet) 
  
            # Put the minimum distance vertex in  
            # the shortest path tree 
            mstSet[u] = True
  
            # Update dist value of the adjacent vertices  
            # of the picked vertex only if the current  
            # distance is greater than new distance and 
            # the vertex in not in the shotest path tree 
            for v in range(self.V): 
                # graph[u][v] is non zero only for adjacent vertices of m 
                # mstSet[v] is false for vertices not yet included in MST 
                # Update the key only if graph[u][v] is smaller than key[v] 
                if self.graph[u][v] > 0 and mstSet[v] == False and key[v] > self.graph[u][v]: 
                        key[v] = self.graph[u][v] 
                        parent[v] = u 
  
        self.printMST(parent)


