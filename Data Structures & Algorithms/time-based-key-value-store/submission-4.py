class TimeMap:

    def __init__(self):
        self.hashMap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hashMap:
            self.hashMap[key] = []
        self.hashMap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hashMap:
            return ""
        vals = self.hashMap[key]
        if not vals:
            return ""
        if vals[0][0] > timestamp:
            return ""
        r = len(vals) - 1
        l = 0
        res = ""

        while l <= r:
            mid = (l + r) // 2
            if vals[mid][0] <= timestamp:
                res = vals[mid][1]
                l = mid + 1
            else:
                r = mid - 1
            
        return res





