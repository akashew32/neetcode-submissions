class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        half = (total + 1) // 2

        if len(B) < len(A):
            A, B = B, A

        l, r = 0, len(A)
        while l <= r:
            i = (l + r) // 2
            j = half - i

            Aleft = A[i - 1] if i > 0 else float("-inf")
            Aright = A[i] if i < len(A) else float("inf")

            Bleft = B[j - 1] if j > 0 else float("-inf")
            Bright = B[j] if j < len(B) else float("inf")

            ## Conditions for if we have found
            if Aleft <= Bright and Bleft <= Aright:
                ## if odd
                if total % 2 == 1:
                    return float(max(Aleft, Bleft))
                else:
                    lmax = max(Bleft, Aleft)
                    rmax = min(Aright, Bright)

                    return float((rmax + lmax) / 2)
            if Bright < Aleft:
                r = i - 1
            else:
                l = i + 1


        
        