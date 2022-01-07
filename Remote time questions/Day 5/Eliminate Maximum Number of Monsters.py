class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        count = 0
        monster = list(zip(dist,speed))
        monster = [[x, y,x/y] for x, y in monster ]
        monster.sort(key = lambda x: x[2])
        for i in monster:
            i[0] = i[0]-i[1]*count
            if i[0] > 0:
                count +=1
            else:
                break
        return count