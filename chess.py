# Design and imoplement for a given chess board having NxN cells. Place N queens on the board such that no queen attacks any other queen. if it is possible to place all the N queens in such a way, then print N lines having N queens. If there is more than one sulution of placing the queens, oprint them all. If it is not possible to place all the of the N queens in the desired way, then print "Not possible"

def is_safe(Board,row,col,N):
    for i in range(col):
        if board[row][i]==1:
            return False
    i = row
    j = col
    while i>= 0 and j>=0:
        if board[i][j]==1:
            return False
        i-=1
        j-=1
    i = row
    j = col
    while j>= 0 and i < N:
        if board[i][j]==1:
            return False
        i+=1
        j-=1
    return True

def solve_n_queens_utils(board,col,N,solutions):
    if col == N:
        solution=[]
        for i in range(N):
            row = []
            for j in range(N):
                row.append(board[i][j])
            solution.append(row)
        solutions.append(solution)
        return
    for i in range(N):
        if is_safe(board,i,col,N):
            board[i][col]=1
            solve_n_queens_utils(board,col,N,solutions)