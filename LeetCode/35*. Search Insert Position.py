class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        result = 0
        if target in nums:
            if nums[l] == target:
                return l
            elif nums[r] == target:
                return r
            else:
                while nums[l] != target and nums[r] != target:
                    l += 1
                    r -= 1
                    if nums[l] == target:
                        result = l
                        break
                    elif nums[r] == target:
                        result = r
                        break
        else:
            if nums[l] > target:
                return l
            elif nums[r] < target:
                return r + 1
            else:
                while nums[l] < target and nums[r] > target:
                    l += 1
                    r -= 1
                    if nums[l] > target:
                        result = l
                        break
                    elif nums[r] < target:
                        result = r + 1
                        break
        return result
        

# not the best runtime