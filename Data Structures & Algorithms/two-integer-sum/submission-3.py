class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for index in range(len(nums)):
            next_item = target - nums[index]
            if next_item in dict:
                return [dict.get(next_item), index]
            dict[nums[index]] = index
