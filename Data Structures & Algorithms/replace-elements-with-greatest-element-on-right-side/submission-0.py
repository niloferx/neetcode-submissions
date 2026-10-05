class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        length = len(arr)
        #right_max = arr[length-1]
        #arr[length-1]=-1
        for i in range(length-1):
            right_max = arr[length-1]
            for j in range(length-1,i,-1):
                if arr[j] > right_max:
                    right_max = arr[j]
            arr[i] = right_max
        arr[-1] = -1
        return arr
