class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [None]*2*n
        #for j in range(len(nums)):
        for j,i in enumerate(nums):
            ans[j]  =  i
            ans[j+n]  =  i

        return ans