class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        
        k = 0
        for i in range(len(nums1)):
           for j in range(k,n):
                if nums1[i] ==0:
                    nums1[i] = nums2[j]
                    k += 1
                    break
        nums1 = nums1.sort()