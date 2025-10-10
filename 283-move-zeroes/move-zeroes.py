class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        new_list = []
        for counter in range(0, len(nums)):
            if nums[counter]!= 0:
                new_list.append(nums[counter])
        while len(new_list) < len(nums):
            new_list.append(0)
            
        for i in range(len(nums)):
            nums[i] = new_list[i]
        
        # Time Complexity - O(N)
        # Space Complexity - O(1) 