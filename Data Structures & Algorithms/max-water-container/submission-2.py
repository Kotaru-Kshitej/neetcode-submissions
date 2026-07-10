class Solution:
    def maxArea(self, h: List[int]) -> int:
        maxx=0
        n=len(h)
        left=0
        right=n-1
        while(left<right):
            area=(right-left)*min(h[left],h[right])
            maxx=max(maxx,area)
            if(h[left]<=h[right]):
                left+=1
            else:
                right-=1
        return maxx