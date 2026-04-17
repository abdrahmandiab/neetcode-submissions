class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        pos_speed = []
        for i in range(n):
            pos_speed.append([position[i],speed[i]])
        pos_speed.sort(key=lambda x: x[0],reverse=True)
        
        timeStack = []
        for pos,speed in pos_speed:
            time = (target - pos) / speed
            timeStack.append(time)
            if len(timeStack) >1:
                prev_time = timeStack[-2]
                if time <= prev_time:
                    timeStack.pop()
            

        return len(timeStack)