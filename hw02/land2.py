from sys import stdin
from collections  import deque
def solve(mx,row,col):
	aux = [[0 for _ in range(col)]for _ in range(row)]
	for i in range(1, R): 
        for j in range(1, C): 
            if (mx[i][j] == 1): 
                aux[i][j] = min(aux[i][j-1], aux[i-1][j], aux[i-1][j-1]) + 1
            else: 
                aux[i][j] = 0
    # Find the maximum entry and 
    # indices of maximum entry in S[][] 
    max_of_s = S[0][0] 
    max_i = 0
    max_j = 0
    for i in range(R): 
        for j in range(C): 
            if (max_of_s < S[i][j]): 
                max_of_s = S[i][j] 
                max_i = i 
                max_j = j

	return 

def main():
	MX = [[0, 1, 1, 0, 1],  
         [1, 1, 0, 1, 0],  
         [0, 1, 1, 1, 0],  
         [1, 1, 1, 1, 0],  
         [1, 1, 1, 1, 1],  
         [0, 0, 0, 0, 0]]
    print(solve(MX),6,5)
main()