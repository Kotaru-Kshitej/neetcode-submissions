class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left=0
        right=len(numbers)-1
        while(left<right):
            summ=numbers[left]+numbers[right]
            if(target>summ):
                left+=1
            elif(target<summ):
                right-=1
            else:
                return[left+1,right+1]
               