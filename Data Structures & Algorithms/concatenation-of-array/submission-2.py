class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return nums * 2
        # or return nums + nums (Python list concatenation)
        # or iterate through each element and assign to new array as below
        #n = len(nums)
        #ans = [None]*2*n
        #for j,i in enumerate(nums):
        #    ans[j]  =  i
        #    ans[j+n]  =  i

        #return ans