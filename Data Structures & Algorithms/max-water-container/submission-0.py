class Solution:
    def maxArea(self, h: List[int]) -> int:
        maxx=0
        n=len(h)
        for i in range(n):
            for j in range(i+1,n):
                maxx=max(maxx,(j-i)*min(h[i],h[j]))
        return maxx