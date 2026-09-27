class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash_map = {}
        for num in nums:
            if num in hash_map: 
                hash_map[num] = hash_map[num] + 1
            else:
                hash_map[num] = 1
            if hash_map[num]>1:
                return True;
                break
        return False