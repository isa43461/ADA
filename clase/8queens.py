def conflict(board,n,x):
    ans,i = False,0
    while not(ans) and i != n:
        ans,i = board[i]==x or n-i == x-board[i] or n-i == board[i]-x,i+1
    return ans

def solve(board,n,ans):
    if n == 8:
        ans.append(list(board))
    else:
        for i in range(8):
            if not conflict(board,n,i):
                board[n] = i
                solve(board,n+1,ans)
        board[n] = None

def main():
    board = [None for _ in range(8)]
    ans = list()
    solve(board,0,ans)
    print(len(ans))
    #for i in ans:
     #   print(i)
    
main()