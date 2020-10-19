class SymbolTable:

    def __init__(self, capacity):
        self.__capacity = capacity
        self.__symbols = [""] * capacity

    def hash(self, key):
        hashval = 0
        j = 1
        for i in key:
            hashval += ord(i) * j
            j = j*10
        return hashval % self.__capacity

    def rehash(self):
        self.__capacity = self.__capacity*2
        symbols = [""] * self.__capacity
        valid = True
        for old in self.__symbols:
            if old:
                hashed_key = self.hash(old)
                if symbols[hashed_key]!="":
                    valid = False
                    self.rehash()
                else:
                    symbols[hashed_key] = old
                if not valid:
                    break
        if valid:
            self.__symbols = symbols

    def insert(self, key):
        hashed_key = self.hash(key)
        while self.__symbols[hashed_key]!="":
            if self.__symbols[hashed_key] == key:
                return
            self.rehash()
            hashed_key = self.hash(key)
        self.__symbols[hashed_key] = key

    def lookup(self, key):
        hashed_key = self.hash(key)
        return self.__symbols[hashed_key]
