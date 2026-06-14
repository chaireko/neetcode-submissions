class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_prefix = [1 for i in range(len(nums))]
        right_prefix = [1 for i in range(len(nums))]
        running_product=1
        for i in range(len(nums)):
            if i == 0:
                running_product*=nums[i]
                continue
            left_prefix[i] = running_product
            running_product*=nums[i]
        running_product=1
        for i in range(len(nums)-1,-1,-1):
            if i == len(nums) - 1:
                running_product*=nums[i]
                continue
            right_prefix[i] = running_product
            running_product*=nums[i]
        ans=[]
        for i in range(len(left_prefix)):
            ans.append(left_prefix[i]*right_prefix[i])
        return ans
        
        # go from left to right, compute product of everythign to left of curr index
        # go from right to left, compute product of everything to right of curr index, else 1

        # multiply every index to get final