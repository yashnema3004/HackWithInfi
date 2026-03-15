class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        for i in range(1,n):
            if nums[i] == nums[i-1]:
                return nums[i]


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        seen = {}
        for i in range(len(nums)):
            if nums[i] in seen:
                return nums[i]
            else:
                seen[nums[i]]  = True

                   

        
            

        
