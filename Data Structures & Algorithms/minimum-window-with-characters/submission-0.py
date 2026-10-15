
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t): 
            return ""
        left = 0
        window_freq = {}
        freq_t = {}
        min_length = float('inf')
        res_left = 0 
        res_right = 0
    
        for i in range(len(t)):
            freq_t[t[i]] = freq_t.get(t[i],0) + 1

        have = 0 
        need = len(freq_t)

    
        for right in range(len(s)): 
            window_freq[s[right]] =  window_freq.get(s[right],0) + 1 

            if s[right] in freq_t and window_freq[s[right]] == freq_t[s[right]]: 
                have +=1 


            while have == need: 
                if min_length > right-left +1:
                    min_length = right-left +1 
                    res_left = left 
                    res_right = right

                window_freq[s[left]] -=1
                if s[left] in freq_t and window_freq[s[left]] < freq_t[s[left]]: 
                    have -=1
                left +=1 
    
        return s[res_left: res_right+1] if min_length != float('inf') else ""





    
   


        











        