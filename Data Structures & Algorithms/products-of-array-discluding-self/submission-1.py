class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_side = []
        right_side = [None]*len(nums)
        res = []
        for i in range(len(nums)):
            if i == 0:
                left_side.append(nums[i])
            else: 
                prod = nums[i] * left_side[i-1]
                left_side.append(prod)
        for i in range(len(nums) -1,-1, -1):
            if i == len(nums) -1:
               right_side[i] = nums[i]
            else:
                prod =  prod = nums[i] * right_side[i+1]
                right_side[i] = prod

        for  i in range(len(nums)):
             if i == 0:
                res.append(right_side[i+1])
             elif i == len(nums)-1:
                res.append(left_side[i-1])
             else:
                res.append(right_side[i+1]*left_side[i-1])
        return res

        
          
        