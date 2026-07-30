class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counts1 = {}
        for i in s1: 
            counts1[i] = counts1.get(i,0) + 1

        l = 0
        k = len(s1)
        for r in range(len(s2)): 
            if r >= k-1:
                window_count = {}
                for c in s2[r-k + 1 : r+1]:
                    window_count[c] = window_count.get(c,0) + 1
                if window_count == counts1: 
                    return True

        return False



        
       
        
        
        

        

       