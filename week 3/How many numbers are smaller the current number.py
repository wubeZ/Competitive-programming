class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        answer = []
        for i in range(len(nums)):
            count = 0
            for j in nums:
                if nums[i] > j:
                    count += 1
            answer.append(count)
        return answer