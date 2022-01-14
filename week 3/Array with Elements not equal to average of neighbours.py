class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        length = len(nums)
        arr = [0]*length
        e = 0
        o = 1
        mid = length//2
        for i in range(mid):
            arr[o] = nums[i]
            o += 2
        for i in range(mid,length):
            arr[e] = nums[i] 
            e += 2
        return arr