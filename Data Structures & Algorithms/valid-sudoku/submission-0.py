class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        box_setter = [i for i in range(9)]
        columns = {i: [] for i in range(9)}
        rows = {i: [] for i in range(9)}
        boxes = { 0: {i: [] for i in range(3)},
                  1: {i: [] for i in range(3)},
                  2: {i: [] for i in range(3)}   }
        print(boxes)
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num != ".":
                    if num in rows[i] or num in columns[j] or num in boxes[int(i/3)][int(j/3)]:
                        return False
                    else:
                        rows[i].append(num)
                        columns[j].append(num)
                        boxes[int(i/3)][int(j/3)].append(num)
        return True