"""
[4] Median of Two Sorted Arrays
https://leetcode.com/problems/median-of-two-sorted-arrays

* Hard (20.05%)
* Total Accepted:    119369
* Total Submissions: 593859

There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays.
The overall run time complexity should be O(log (m+n)).

Example 1:

nums1 = [1, 3]
nums2 = [2]

The median is 2.0



Example 2:

nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
"""


class Solution(object):
    # Time: O(n + log2)
    # Space: O(n)
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        merged = sorted(nums1 + nums2)
        merge_len = len(merged)
        if merge_len % 2 == 0:
            half = merge_len // 2
            return (merged[half] + merged[half-1])/float(2)
        else:
            return float(merged[merge_len//2])

    # https://github.com/kamyu104/LeetCode/blob/master/Python/median-of-two-sorted-arrays.py
    # Time: O(log(min(m, n))
    # Space: O(1)
    def findMedianSortedArrays_kamyu(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        len1, len2 = len(nums1), len(nums2)
        if (len1 + len2) % 2 == 1:
            return self.getKth(nums1, nums2, (len1 + len2)/2 + 1)
        else:
            return (self.getKth(nums1, nums2, (len1 + len2)/2) +
                    self.getKth(nums1, nums2, (len1 + len2)/2 + 1)) * 0.5

    def getKth(self, A, B, k):
        m, n = len(A), len(B)
        if m > n:
            return self.getKth(B, A, k)

        left, right = 0, m
        while left < right:
            mid = left + (right - left) / 2
            if 0 <= k - 1 - mid < n and A[mid] >= B[k - 1 - mid]:
                right = mid
            else:
                left = mid + 1

        Ai_minus_1 = A[left - 1] if left - 1 >= 0 else float("-inf")
        Bj = B[k - 1 - left] if k - 1 - left >= 0 else float("-inf")

        return max(Ai_minus_1, Bj)


if __name__ == '__main__':
    nums1 = [1, 2]
    nums2 = [3, 4]
    s = Solution()
    print(s.findMedianSortedArrays(nums1, nums2))
