class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        count = []
        minutes = list(map(lambda x: int(x[:2]) * 60 + int(x[3:]), timePoints))
        minutes.sort()
        minutes_zip = list(zip(minutes,minutes[1:] + minutes[:1]))
        for x, y in minutes_zip:
            count.append((y-x)%1440)
        return (min(count))