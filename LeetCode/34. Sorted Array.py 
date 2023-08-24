class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l = 0
        r = len(nums) - 1
        if target not in nums:
            return [-1, -1]
        else:
            while nums[l] != target or nums[r] != target:
                if nums[l] != target:
                    l += 1
                if nums[r] != target:
                    r -= 1
                if l == len(nums) - 1 and r == 0:
                    return [-1, -1]
        return [l, r]
        
            
# not very efficient. learn how to do it from the middle.
