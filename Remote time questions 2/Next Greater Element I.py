class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d = defaultdict(lambda:-1)
        stack = []
        answer = []
        for i in nums2:
            while stack and stack[-1] < i:
                d[stack.pop()] = i
            stack.append(i)
    
        for j in nums1:
            answer.append(d[j])
            
        return answer