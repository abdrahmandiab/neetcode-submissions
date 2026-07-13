class CountSquares:

    def __init__(self):
        self.ptsCount = defaultdict(lambda:defaultdict(int))

    def add(self, point: List[int]) -> None:
        self.ptsCount[point[0]][point[1]] +=1

    def count(self, point: List[int]) -> int:
        res = 0
        x1,y1 = point
        for y2 in self.ptsCount[x1]:
            if y2 == y1:
                continue
            side = y2-y1

            x3, x4 = x1+side, x1-side
            
            res += (self.ptsCount[x1][y2] * self.ptsCount[x3][y1] * self.ptsCount[x3][y2])
            res += (self.ptsCount[x1][y2] * self.ptsCount[x4][y1]* self.ptsCount[x4][y2])
        return res

# for point [2,1]
# need point at p1 [2,2], point at p2 [1,1], point at p3 [1,2]
# but could've also had: pt at [2,3], [0,1], [0,3]
# or  [2,4], [-1,1], [-1,4]
# pattern is:
# for p1 = top right, p2 = bottom left, p3 = top left, p4 = bottom right
# p1.x == p4.x
# p1.y == p3.y
# p2.y == p4.y
# p3.x == p2.x

# pitfalls:
# must check not only to top and right, but also to left and bottom
