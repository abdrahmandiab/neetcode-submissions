class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos_speed = [(p,s) for p,s in zip(position,speed)]
        pos_speed.sort(reverse=True) # [(7,2),(4,2),(1,1),(0,1)]
        time_stack = []
        print(pos_speed)
        print(pos_speed[1::])
        for p,s in pos_speed:
            t = (target - p) / s# target = pos + speed*time
            time_stack.append(t)
            if len(time_stack)>1 and time_stack[-2] >= t:
                time_stack.pop()                

        return len(time_stack)