class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        output = []
        for counter1 in range(0, len(nums1)):
            for counter2 in range(0, len(nums2)):
                if nums1[counter1] == nums2[counter2] and nums1[counter1] not in output:
                    output.append(nums1[counter1])
        return output