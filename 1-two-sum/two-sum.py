class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}
        for counter in range(len(nums)):
            current_element = nums[counter]
            needed_element = target - current_element

            if needed_element in num_map:
                return [counter, num_map[needed_element]]
                
            num_map[current_element] = counter

