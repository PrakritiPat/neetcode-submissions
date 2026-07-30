class Solution:
    def into_binary(self,n):
        if n == 0:
            return "0"
        bits = []
        while n > 0:
            remainder = n%2
            bits.append(str(remainder))
            n//=2
        bits.reverse()
        answer = "".join(bits)
        return answer

        
    

    def countBits(self, n: int) -> List[int]:
        res = []
        
        number_of_ones = []
        for i in range(0,n+1):
            res.append(self.into_binary(i))
        for n in res:
            number_of_ones.append(n.count("1"))
        return number_of_ones
            


        

        
  

        
