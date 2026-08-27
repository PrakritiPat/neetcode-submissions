class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row = len(board)
        col = len(board[0])
        


        def backtrack(row,col,i):
            #base case: return true if path == word

            if i == len(word): 
                return True

            if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]): 
                return False

            if board[row][col] != word[i]:
                return False


            
            if board[row][col] == word[i]:
                temp = board[row][col]
                board[row][col] = '#'



                found = (backtrack(row+1,col,i+1) or backtrack(row-1,col, i+1) or backtrack(row,col+1,i+1) or backtrack(row,col-1,i+1))
                board[row][col] = temp

                return found


        for i in range(row):
            for j in range(col): 
                if backtrack(i,j,0):
                    return True
        return False
    
    


                
    

          

                   
                        



        