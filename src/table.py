try:
    from src.hash import hash_string
except ImportError:
    from hash import hash_string

class Table:
    def __init__(self):
        self._items = {}

    @property
    def items(self):
        return self._items

    def add(self, key, value):
        hashed_key = hash_string(key)
        self._items[hashed_key] = value

    def delete(self, key):
        hashed_key = hash_string(key)
        del self._items[hashed_key]

    def get(self, key):
        hashed_key = hash_string(key)
        return self._items[hashed_key]

    def contains(self, key):
        hashed_key = hash_string(key)
        return hashed_key in self._items

    def __str__(self):
        return str(self._items)

    def __repr__(self):
        return str(self._items)

    def __len__(self):
        return len(self._items)