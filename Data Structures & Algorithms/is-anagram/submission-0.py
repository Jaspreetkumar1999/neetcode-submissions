class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
       if len(s) != len(t): 
           return False
       s_dict = {}
       t_dict = {}
       for i in s:
        if i in s_dict: 
            s_dict[i] = s_dict[i]+1
        else: 
            s_dict[i] = 1
       for j in t: 
         if j in t_dict:
            t_dict[j] = t_dict[j]+1
         else: 
            t_dict[j] = 1
       print("++s__dic", s_dict)
       print("++T_DICT", t_dict)
        
       for key in s_dict:
        if key not in t_dict:
            return False
            break
        if s_dict[key] != t_dict[key]:
            return False
            break
       return True

        
            

        