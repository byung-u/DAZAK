class Solution(object):
    def twoSum(self, nums, target):
        # Time:  O(n)
        # Space: O(n)
        lookup = {}
        for i, num in enumerate(nums):
            if target - num in lookup:
                return [lookup[target - num], i]
            lookup[num] = i
        return []
        '''
        # Time:  O(n²)
        # Space: O(n)
        for i in range(len(nums)):
            if (target > 0 and nums[i] > target and nums[i] != 0):
                continue
            elif (target < 0 and nums[i] < target and nums[i] != 0):
                continue

            for j in range(i+1, len(nums)):
                if (target - nums[i] == nums[j]):
                    return [i, j];
        '''