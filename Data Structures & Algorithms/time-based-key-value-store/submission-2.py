class TimeMap:

    def __init__(self):
        self.timemap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.timemap:
            self.timemap[key].append((timestamp, value))
        else:
            self.timemap[key] = [(timestamp, value)]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timemap:
            return ""

        moods = self.timemap[key]
        l = 0
        r = len(moods)
        ans = ""

        while l < r:
            mid = (l + r) // 2

            if moods[mid][0] <= timestamp:
                ans = moods[mid][1]
                l = mid + 1
            else:
                r = mid

        return ans