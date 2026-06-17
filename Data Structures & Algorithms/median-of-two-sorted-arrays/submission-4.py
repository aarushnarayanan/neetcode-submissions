class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2

        # Always binary search on the smaller array
        if len(A) > len(B):
            A, B = B, A

        total = len(A) + len(B)
        half = total // 2
        l, r = 0, len(A)

        while l <= r:
            i = (l + r) // 2        # partition index for A
            j = half - i            # partition index for B

            A_left  = A[i - 1] if i > 0      else float("-inf")
            A_right = A[i]     if i < len(A) else float("inf")
            B_left  = B[j - 1] if j > 0      else float("-inf")
            B_right = B[j]     if j < len(B) else float("inf")

            if A_left <= B_right and B_left <= A_right:
                # Found the correct partition
                if total % 2:
                    return float(min(A_right, B_right))
                return (max(A_left, B_left) + min(A_right, B_right)) / 2.0
            elif A_left > B_right:
                r = i - 1
            else:
                l = i + 1