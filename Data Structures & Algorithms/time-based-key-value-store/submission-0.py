class TimeMap:

    def __init__(self):
        self.store = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store: 
            self.store[key] = []
        self.store[key].append([timestamp, value])

        
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        value = self.store[key]
        low = 0
        high = len(value)-1
        res = ""
        while(low <= high): 
            mid = low + (high-low) //2
            if value[mid][0] == timestamp:
                return value[mid][1]

            if value[mid][0] < timestamp: 
                res = value[mid][1]
                low = mid + 1
            else: 
                high = mid -1 
        return res
        
        
