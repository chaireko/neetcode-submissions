class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # start p2 from end of array
        # move p2 left until not equal to/greater than target
        
        # while p1 < p2 and not equal
            # add p1 and p2
                # if sum is greater, move p2 to left
                # if sum is lesser, move p1 to right
        p1, p2 = 0, len(numbers) - 1
        while p1 < p2 and not p1 == p2:
            total = numbers[p1] + numbers[p2]
            if total > target:
                p2 -= 1
            elif total < target:
                p1 += 1
            else:
                return [p1+1, p2+1]
        