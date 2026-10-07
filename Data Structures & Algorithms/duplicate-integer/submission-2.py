class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #unique = set(nums)
        #if len(unique) != len(nums):
        #    return True
        #return False

        #improved early exit with set
        hashset = set()
        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False