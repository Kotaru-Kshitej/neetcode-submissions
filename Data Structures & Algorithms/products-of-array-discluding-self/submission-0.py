class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res=[]
        i=0
        while i<len(nums):
            pro=1
            for j in range(0,len(nums)):
                if j==i:
                    continue
                else:
                    pro*=nums[j]
            res.append(pro)
            i+=1
        return res