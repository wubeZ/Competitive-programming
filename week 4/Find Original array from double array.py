class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        changed.sort()
        counter = Counter(changed)
        answer = []
        n = len(changed)
        if (n % 2 == 0):
            for i  in changed:
                if(counter[i] > 0 and counter[2*i]):
                    if(i != 0):
                        answer.append(i)
                        counter[i] -= 1
                        counter[2*i] -= 1
                    elif(counter[i] > 1 ):
                        answer.append(i)
                        counter[i] -= 1
                        counter[2*i] -= 1
        if len(answer) == n // 2:
            return answer
        else:
            return [] 