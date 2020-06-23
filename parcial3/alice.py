def solve(G,nodos):
	global indeg, INF
	cont = 0; menor = min(indeg); mayor  = max(indeg)
	i0 = indeg.index(menor); i1 = indeg.index(mayor); band = False
	while((menor < 5 or (nodos-cont) - mayor < 5) and band != True):
		if(menor < 5):
			indeg[i0] = 0
			cont += 1
			for u in G[i0]:
				nm = G[u].index(i0)
				G[u].pop(nm)
				indeg[u] -= 1
			G[i0] = []
		if((nodos-cont) - mayor < 5):
			indeg[i1] = 0
			cont += 1
			for u in G[i1]:
				nm = G[u].index(i1)
				G[u].pop(nm)
				indeg[u] -= 1
			G[i1] = []
		paux = 0
		INF = float('inf')
		for i in range(nodos):
			if(sum(indeg) != 0):
				if(indeg[i] < INF and indeg[i] != 0):
					INF = indeg[i]; paux = i
			else: band = True
		menor,mayor = INF, max(indeg)
		i0,i1 = paux,indeg.index(mayor)
	return G

def main():
	global indeg
	A = [(0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (2, 3), (2, 6), (2, 4), (2, 5), (3, 6), (3, 4), (3, 5), (6, 4), (6, 5), (4, 5), (1, 7), (1, 8), (1, 9), (1, 10), (1, 11), (7, 8), (7, 9), (7, 10), (7, 11), (8, 9), (8, 10), (8, 11), (9, 10), (9, 11), (10, 11), (12, 2), (12, 7), (13, 5), (13, 10)]
	A0 = [(0,1),(0,2),(0,3),(0,4),(0,5),(1,2),(1,3),(1,4),(1,5),(2,3),(2,4),(2,5),(3,4),(3,5),(4,5),(6,1)]
	n = len(A); #nodos = 14; n0 = len(A0)
	nodos = 14
	indeg = [0 for _ in range(nodos)]
	for u in range(n):
		for v in A[u]:
			indeg[v] += 1
	G = [[] for i in range(nodos)]
	for i in range(n):
		G[A[i][0]].append(A[i][1])
		G[A[i][1]].append(A[i][0])
	ans = 0
	solve(G,nodos)
	#print("ind0", indeg)
	for i in range(nodos):
		if(indeg[i] != 0):
			ans +=1
	print(ans)
main()