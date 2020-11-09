class FAReader:
    def __init__(self, filename):
        file = open(filename, "r")
        lines = file.readlines()
        file.close()
        self.__states = lines[0].strip().split(" ")
        self.__symbols = lines[1].strip().split(" ")
        self.__initial = lines[2].strip()
        self.__final = lines[3].strip().split(" ")
        self.__transitions = {}
        for i in range(4, len(lines)):
            elems = lines[i].strip().split(" ")
            if (elems[0], elems[1]) in self.__transitions:
                self.__transitions[(elems[0], elems[1])].append(elems[2])
            else:
                self.__transitions[(elems[0], elems[1])] = [elems[2]]

    def print_states(self):
        result = "["
        for i in self.__states:
            result += i + " "
        result = result[:-1] +  "]"
        return result

    def print_symbols(self):
        result = "["
        for i in self.__symbols:
            result += i + " "
        result = result[:-1] +  "]"
        return result

    def print_transitions(self):
        result = "{"
        for i in self.__transitions:
            result += "[(" + i[0] + ", " + i[1] + ") " + "-> " + "["
            for j in self.__transitions[i]:
                result+= j + ", "
            result+= "]], "
        result = result[:-2] +  "}"
        return result

    def print_final(self):
        result = "["
        for i in self.__final:
            result += i + " "
        result = result[:-1] +  "]"
        return result

    def menu(self):
        while True:
            option = input("1.Display set of states.\n2.Display alphabet.\n3.Display all transitions.\n4.Display final states.\n5.Exit.\n")
            if option=="1":
                print("The set of states: " + self.print_states())
            elif option == "2":
                print("The alphabet: " + self.print_symbols())
            elif option == "3":
                print("All transitions: " + self.print_transitions())
            elif option == "4":
                print("Final states: " + self.print_final())
            elif option == "5":
                return
            else:
                print("Invalid command!")

f = FAReader("FA.in")
f.menu()