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
            # we already have x1, y1, and y2
            # since we have the side length,
            # we can now calculate all the other possible points
            # i.e. if x1,y1 is bottom left point of square
            #  x1 = x3, y1 = y4
            #  x2 = x1, y2 = y3
            #  x3 = x4 = x1+side_length (or x1-side_length) , y3 = y2
            #  x4 = x3, y4 = y1
            x2 = x1
            y3 = y2
            y4 = y1
            x3 = x4 = x1+side
            res += (self.ptsCount[x2][y2] * self.ptsCount[x3][y3] * self.ptsCount[x4][y4])
            x3 = x4 = x1-side
            res += (self.ptsCount[x2][y2] * self.ptsCount[x3][y3] * self.ptsCount[x4][y4])
        return res

# for point [2,1]
# need point at p1 [2,2], point at p2 [1,1], point at p3 [1,2]
# but could've also had: pt at [2,3], [0,1], [0,3]
# or  [2,4], [-1,1], [-1,4]
# pattern is:
# for p1 = top right, p2 = bottom left, p3 = top left, p4 = bottom right


# pitfalls:
# must check not only to top and right, but also to left and bottom
