class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        map = {}
        count = 1
        for i in range(len(position)):
            map[position[i]] = speed[i]

        position.sort()
        times = []
        for i in range(len(position)):
            pos = position[i]
            time = (target - pos) / (map[pos])
            times.append(time)
        
            
        times.reverse()
        print(times)
        temp = times[0]
        for i in range(len(times)):
            if times[i] > temp:
                count += 1
                temp = times[i]
         
        return count


