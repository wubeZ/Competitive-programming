class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr = []
        freqarr= Counter(arr1)
        for i in arr2:
            arr += [i] * freqarr[i]
            del freqarr[i]
        restelem = freqarr.elements()
        restelem  = sorted(restelem)
        for i in range(len(restelem)):
            arr.append(restelem[i])
        return arr