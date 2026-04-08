class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(A) + len(B)
        half = total // 2

        if len(A) > len(B):
            A, B = B, A

        l, r = 0, len(A)
        while True:
            i = (l + r) // 2 #A
            j = half - i #B

            Aleft = A[i - 1] if i > 0 else float("-inf")
            Aright = A[i] if i < len(A) else float("inf")
            Bleft = B[j - 1] if j > 0 else float("-inf")
            Bright = B[j] if j < len(B) else float("inf")

            if Aleft <= Bright and Bleft <= Aright:
                if total % 2 != 0:
                    return min(Aright, Bright)
                else:
                    return (max(Bleft, Aleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright:
                r = i - 1
            else: l = i + 1






        