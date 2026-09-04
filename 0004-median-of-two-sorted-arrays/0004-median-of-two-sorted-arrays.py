import numpy as np
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merge = nums1 + nums2
        data = np.array(merge)
        return np.median(data)
