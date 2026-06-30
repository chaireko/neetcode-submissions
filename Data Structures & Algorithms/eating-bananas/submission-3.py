class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        while left < right:
            mid = (left+right)//2
            # calculate total hrs w/ mid
            total_time=0
            for i in range(len(piles)):
                total_time+=(piles[i]+mid-1)//mid
            if total_time > h:
                left = mid+1
            else:
                right = mid
        return left
        
