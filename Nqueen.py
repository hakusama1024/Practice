def solveNQueens(n):
    """
    :type n: int
    :rtype: List[List[str]]
    """
    def check(k,j,board):
        for i in range(k):
            if board[i]==j or abs(k-i)==abs(board[i]-j):
                return False
        return True
    def dfs(depth,board,valuelist,solution):
        if depth==len(board):
            solution.append(valuelist)
        for row in range(len(board)):
            if check(depth,row,board):
                s='.'*len(board)
                board[depth]=row
                dfs(depth+1,board,valuelist+[s[:row]+'Q'+s[row+1:]],solution)
    board=[-1 for i in range(n)]
    solution=[]
    dfs(0,board,[],solution)
    return solution

print solveNQueens(8)
