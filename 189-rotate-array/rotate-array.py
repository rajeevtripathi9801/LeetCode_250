class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        size = len(nums)
        k = k% size

        def reverse_helper(start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1 
                end -= 1
        
        reverse_helper(0, size - 1)
        reverse_helper(0, k - 1)
        reverse_helper(k, size - 1)