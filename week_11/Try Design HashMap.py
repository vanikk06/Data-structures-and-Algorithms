class MyHashMap:

    def __init__(self):
        self.dic = {}

    def put(self, key: int, value: int) -> None:
        if key not in self.dic:
            self.dic[key] = value
        else:
            self.dic[key] = value
        

    def get(self, key: int) -> int:        
        if key in self.dic:
            return self.dic[key]
        else:
            return -1
        

    def remove(self, key: int) -> None:        
        if key in self.dic:
            self.dic.pop(key)
