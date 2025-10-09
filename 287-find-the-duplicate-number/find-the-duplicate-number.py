class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        size = len(nums)
        nums.sort()

        for counter in range(0, size):
            if nums[counter] == nums[counter + 1]:
                return nums[counter]