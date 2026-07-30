class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        string_res = ""
        for i in range(len(digits)):
            digits[i] = str(digits[i])
            string_res += digits[i]
        int_res = int(string_res)
        int_res+=1
        string_res2 = str(int_res)
        final_res = []
        for s in string_res2:
            final_res.append(s)
        return final_res

        