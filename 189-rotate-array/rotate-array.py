class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        size_of_array = len(nums)
        k %= size_of_array      # To handle cases k>n 
        temp = [0] * size_of_array
        
        for counter in range(size_of_array):
            temp[(counter + k) % size_of_array] = nums[counter]
        
        for counter in range(size_of_array):
            nums[counter] = temp[counter]  
