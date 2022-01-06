class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        answer = []
        nums.sort()
        length = len(nums) 
        for j in range(1,length):
                if nums[j] == nums[j-1]:
                   answer.append(nums[j])
                   nums.remove(nums[j])
                   break
        for i in range(1,length + 1):
            if i not in nums:
                answer.append(i)
        return answer     
        