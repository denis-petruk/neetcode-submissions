class MyHashMap:

    def __init__(self):
        self.hash_map = list()

    def put(self, key: int, value: int) -> None:
        for index,hash_set in enumerate(self.hash_map):
            if hash_set[0] == key:
                self.hash_map[index][1] = value
                return None
        self.hash_map.append([key,value])

    def get(self, key: int) -> int:
        for i in self.hash_map:
            if i[0] == key:
                return i[1]
        return -1

    def remove(self, key: int) -> None:
        for i in self.hash_map:
            if i[0] == key:
                self.hash_map.remove([i[0],i[1]])
                break