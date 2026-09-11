class MyHashSet:
    def __init__(self):
        self.bucket_count = 769
        self.buckets = [[] for _ in range(self.bucket_count)]

    def _hash(self, key: int) -> int:
        return key % self.bucket_count

    def add(self, key: int) -> None:
        idx = self._hash(key)
        bucket = self.buckets[idx]
        if key not in bucket:
            bucket.append(key)

    def remove(self, key: int) -> None:
        idx = self._hash(key)
        bucket = self.buckets[idx]
        if key in bucket:
            bucket.remove(key)

    def contains(self, key: int) -> bool:
        idx = self._hash(key)
        bucket = self.buckets[idx]
        return key in bucket
