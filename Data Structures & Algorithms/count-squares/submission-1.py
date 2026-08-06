class CountSquares:

    def __init__(self):
        self.xVals = defaultdict(list)
        self.coords = defaultdict(int)

    def add(self, point: List[int]) -> None:
        x, y  = point
        self.xVals[x].append(y)
        self.coords[(x, y)] += 1

    def count(self, point: List[int]) -> int:
        res = 0
        x = point[0]
        if x not in self.xVals:
            return res
        for y in self.xVals[x]:
            if y == point[1]:
                continue
            dy = abs(point[1] - y)
            res += self.coords[(x + dy, y)] * self.coords[(x+dy, point[1])]
            res += self.coords[(x-dy, y)] * self.coords[(x-dy, point[1])]

        return res
            