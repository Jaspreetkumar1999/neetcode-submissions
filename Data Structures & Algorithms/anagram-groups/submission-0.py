class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        list = [];
        dict = {};
        for index in range(len(strs)):
           sorted_el = ''.join(sorted(strs[index]))
    
           if sorted_el in dict:
              dict[sorted_el].append(strs[index])
           else: 
              dict[sorted_el] = [strs[index]]
             
        for key in dict: 
            list.append(dict[key])
        return list

        
