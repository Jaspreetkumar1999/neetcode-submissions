class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict = {}
        current_max = 0
        for num in nums:
            if num in dict:
                dict[num] = dict[num] +1
            else: 
                dict[num] = 1
# do it with bucket sort
        sorted_dict = sorted(dict, key= dict.get, reverse = True)
        return sorted_dict[:k]
     