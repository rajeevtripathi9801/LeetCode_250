class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = [0] * (2 * len(nums))  

        size_of_array = len(nums)
        for counter in range(size_of_array):
            ans[counter] = nums[counter]
            ans[counter + size_of_array] = nums[counter]
        return ans
        