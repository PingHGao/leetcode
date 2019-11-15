class LRUCache:

    def __init__(self, capacity: int):
        from collections import OrderedDict
        self.cache = OrderedDict()
        self.maxsize = capacity

    def get(self, key: int) -> int:
        res = self.cache.get(key)
        if not res:
            res = -1
        else:
            self.cache.move_to_end(key)
        
        return res
        

    def put(self, key: int, value: int) -> None:
        self.cache[key] = value
        self.cache.move_to_end(key)
        if len(self.cache) > self.maxsize:
            self.cache.popitem(last=False)
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
