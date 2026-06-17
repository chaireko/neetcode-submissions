class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # combine positions and speeds
        # sort desc by position
        # for each position, calculate time 
            # if time is less than car ahead time, then move on
            # if time is greater than car ahead time, add to stack
        cars = []
        stack = []
        prev_t = -1
        for i in range(len(position)):
            cars.append((position[i], speed[i]))
        cars_desc = sorted(cars, key=lambda x: x[0], reverse=True)
        for i in range(len(cars_desc)):
            t = (target-cars_desc[i][0])/cars_desc[i][1]
            stack.append(t)
            if t <= prev_t:
                stack.pop()
            else:
                prev_t = t

        return len(stack)
