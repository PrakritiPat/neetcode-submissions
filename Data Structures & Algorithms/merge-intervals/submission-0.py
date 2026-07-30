class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        res = [intervals[0]]
        for i in intervals:
            last = res[-1]
            if i[0] <= last[1]:
                last[1] = max(last[1],i[1])
            else: 
                res.append(i)
        return res




        
        

            
        