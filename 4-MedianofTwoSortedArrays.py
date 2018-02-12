class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        num = sorted(nums1 + nums2)
        length = len(num)
        if (length%2) == 0:
            return (num[int(length/2)-1]+num[int(length/2)])/2
        else:
            return float(num[int(length/2)])
