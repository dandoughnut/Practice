class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 1
        if len(nums) > 1:
            while k < len(nums):
                if nums[k] == nums[k-1]:
                    if k == len(nums) - 1:
                        return k
                    else:
                        while nums[k] == nums[k-1]:
                            nums.pop(k)
                            if k == len(nums)-1:
                                break
                            
                else:
                    k += 1
                    if k == len(nums):
                        break
                
        return k

# Inefficient solution that performs poorly in terms of runtime.
# Use the set method next time