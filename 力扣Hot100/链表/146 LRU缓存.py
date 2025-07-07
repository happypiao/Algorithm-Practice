class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.values = {}

    def get(self, key: int) -> int:
        return self.values.get(key, -1) or -1

    def put(self, key: int, value: int) -> None:
        pass

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)