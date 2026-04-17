class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        pos_speed = [(p,s) for p,s in zip(position,speed)]
        pos_speed.sort(reverse=True)

        timeStack = []
        for pos , speed in pos_speed:
            time = (target - pos) / speed
            timeStack.append(time)
            if len(timeStack) >1:
                prev_time = timeStack[-2]
                if time <= prev_time:
                    timeStack.pop()
            

        return len(timeStack)