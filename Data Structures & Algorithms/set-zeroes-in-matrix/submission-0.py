class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        n=len(matrix)
        m=len(matrix[0])
        row=[]
        col=[]
        for i in range(n):
            for j in range(m):
                if matrix[i][j]==0:
                    row.append(i)
                    col.append(j)
        for i in range(n):
            for j in range(m):
                if i in row or j in col:
                    matrix[i][j]=0
                
                    

        
        