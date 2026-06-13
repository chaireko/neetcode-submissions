class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # get starting nums
        # for each starting num
        # find consec num in arr
        # keep a max consec num
        starting_nums=[]
        hashset = set(nums)
        for n in nums:
            if n-1 not in hashset:
                starting_nums.append(n)
        occ = 1
        max_occ = 0
        for n in starting_nums:
            i = n+1
            while i in hashset:
                occ += 1
                i+=1
            max_occ = max(max_occ, occ)
            occ = 1
        return max_occ