class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        check=True
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                check=False
        if check:
            return(False)
        else:
            return(True)
            