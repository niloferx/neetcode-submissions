class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Iterative approach
        #left, right = 0, len(nums) - 1
        #while left <= right:
        #    mid = left + (right-left)//2
        #    if nums[mid] == target:
        #        return mid
        #    elif nums[mid] < target:
        #        left = mid + 1
        #    else:
        #        right = mid - 1
        #return -1

        #Recursive approach
        def bs(left:int, right:int) -> int:
            if left > right:
                return -1
            mid = left + (right - left)//2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                return bs(mid+1, right)
            return bs(left, mid-1)

        return bs(0, len(nums)-1)