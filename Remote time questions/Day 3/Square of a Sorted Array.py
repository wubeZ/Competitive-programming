class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        answer = []
        for i in nums:
            answer.append(i**2)
        answer.sort()
        return answer