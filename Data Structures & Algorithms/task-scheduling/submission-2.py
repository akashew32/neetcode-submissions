class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        arr = [[0, x] for x in range(26)]
        temp = []
        count = 0
        for task in tasks:
            arr[ord(task) - ord("A")][0] -= 1
        
        heapq.heapify(arr)
        while arr and arr[0][0] != 0:
            for i in range(n + 1):
                if arr and arr[0][0] != 0:
                    curr = heapq.heappop(arr)
                    curr[0] += 1
                    if curr[0] != 0:
                        temp.append(curr)
                    print(curr[1])
                    count += 1
                else:
                    if temp:
                        count += 1
            while temp:
                pair = temp.pop()
                heapq.heappush(arr, pair)
        return count
        
