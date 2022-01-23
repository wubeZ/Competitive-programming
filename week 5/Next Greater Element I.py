class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        result = []
        d = defaultdict(lambda: -1)
        for i in nums2:
            while len(stack) > 0 and stack[-1] < i:
                d[stack.pop()] = i
            stack.append(i)
        
        for j in nums1:
            result.append(d[j])
        return result   