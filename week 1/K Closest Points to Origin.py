class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points.sort(key = self.calculateDis)
        
        return points[0:k]
    
    def calculateDis(self,point):
        return sqrt(point[0]**2 +point[1]**2)