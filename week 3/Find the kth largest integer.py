class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        index  = len(nums) - k
        nums.sort(key = lambda x: int(x))
        print(nums)
        return nums[index]