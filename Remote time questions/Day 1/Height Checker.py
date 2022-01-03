class Solution:
    def heightChecker(self, heights: List[int]) -> int:  
        height = heights
        expected = sorted(heights)
        count = 0
        for i in range(0,len(heights)):
            if height[i] != expected[i]:
                  count +=1
        return count