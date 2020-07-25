class Solution:
    def min_num_clicks(self,board):
        def matrix_print(matrix):
            for row in matrix:
                print(row)
            print('')

        def zadd(coeff,y,i,j):
            for k in range(M*N):
                coeff[j][k] = (coeff[j][k] + coeff[i][k]) & 1
            y[j] = (y[i] + y[j]) & 1

        if not board or not board[0]: return -1
        print('Initial board is:')
        matrix_print(board)

        M = len(board)
        N = len(board[0])
        coeff = [[0]*(N*M) for _ in range(M*N)]
        y = [0]*(N*M)

        ### Generate coeff matrix ###
        for i,row in enumerate(board):
            for j,n in enumerate(row):
                index=i*N+j
                if n==1: y[index] = 1
                for ii,jj in [(i-1,j),(i,j-1),(i,j),(i+1,j),(i,j+1)]:
                    if 0<=ii<M and 0<=jj<N:
                        coeff[index][ii*N+jj] = 1

        print("coeff",coeff)
        print("y",y)
        ### Gaussian elimination phase 1 ###
        for i in range(M*N-1):
            for j in range(i,M*N):
                if coeff[j][i] == 1:
                    coeff[j],coeff[i] = coeff[i],coeff[j]
                    y[j],y[i] = y[i],y[j]
                    break
                else:
                    continue
            for j in range(i+1,M*N):
                if coeff[j][i] == 1:
                    zadd(coeff,y,i,j)

        ### Gaussian elimination phase 2 ###
        for i in range(M*N-1,0,-1):
            for j in range(i-1,-1,-1):
                if coeff[j][i] == 1:
                    zadd(coeff,y,i,j)

        ### Validate and collect results ###
        clicks = []
        res = 0
        for i in range(M*N):
            if y[i]==1:
                if coeff[i][i]==1:
                    res += 1
                    clicks.append((i//N,i%N))
                else:
                    print('No solution exists')
                    return -1
        print(f'Minimum clicks needed is {res}: {clicks}')
        return res

if __name__=='__main__':
    ##board = [[0,1,0],[1,1,0],[0,1,1]]
    ##board = [[0,0,0],[0,0,1],[0,0,0]]
    ##board = [[1,0,0],[0,0,0]]
    ##board = [[0,0,0,0],[0,0,1,0],[0,0,0,0]]
    board = [[0,1,1,1],[1,0,1,0],[0,1,1,1],[0,0,0,0]]
    Solution.min_num_clicks(None,board)