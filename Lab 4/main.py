import re

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
        return hashed_key

    def lookup(self, key):
        hashed_key = self.hash(key)
        return self.__symbols[hashed_key]

    def __str__(self):
        print(self.__symbols)

class Scanner:

    # This implementation is currently incomplete.

    # TODO:
    # add check if constant
    # properly extract separators with regex
    # make genPIF work


    def __init__(self, token):
        self.st= SymbolTable(10)

        tokens = open(token, "r")
        split_token = tokens.read().split("\n")
        self.reserved_words = []
        self.sep_op = []
        for i in range(9, 21):
            self.reserved_words.append(split_token[i])
        for i in range(0, 9):
            self.sep_op.append(split_token[i])
        tokens.close()

    def genPIF(self, token, index):
        pass

    def scan(self, filename):
        f = open(filename, "r")
        self.file_text = f.readlines()
        f.close()

        printed = False
        for i in range(0, len(self.file_text)):
            j = self.file_text[i].strip().split(" ")
            for k in j:
                z = re.split()
                print(k)
                if k in self.reserved_words or k in self.sep_op:
                    self.genPIF(k, 0)
                elif re.match('[a-zA-Z][a-zA-Z0-9_]*', k):
                    index = self.st.lookup(k)
                    self.genPIF(k, index)
                else:
                    print("Lexical error on line " + str(i+1) + ", \"" + k + "\"")
                    printed = True
        if not printed:
            print("Lexically correct")



y = Scanner("token.in")
y.scan("p1.in")
y.scan("p2.in")
y.scan("p3.in")
y.scan("p1err.in")
