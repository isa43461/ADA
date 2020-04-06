INF = -float('inf')

def solve(X,W,T,i,ans):
	global INF
	acum = 0
	if(i == 0):
		if(T == 0):
			for n in ans:
				acum += W[n]
			#print(acum, ans, X[ans[0]], X[ans[1]])
			if(acum > INF):
				INF = acum
	else:
		solve(X,W,T,i-1,ans)
		if(X[i-1] <= T):
			ans.append(i-1)
			solve(X,W,T-X[i-1],i-1,ans)
			ans.pop()

def main():
    X = [3,7,5,1]
    W = [2,4,3,2]
    X2 = [1,2,4,5,2,1] 
    W2 = [2,1,6,3,1,1]
    T = 8
    ans = list()
    solve(X,W,T,len(X),ans)
    print("El peso máximo del subconjunto X cuyos elementos suma a T es: ",INF)
    T = 5
    solve(X2,W2,T,len(X),ans)
    print("El peso máximo del subconjunto X cuyos elementos suma a T es: ",INF)
    #se colaboró con Camilo Gutierrez
main()