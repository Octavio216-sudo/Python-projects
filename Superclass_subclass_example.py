class stack():
    def __init__(self, val):
        self.__stk_list = [] 
        self.__val = val
    def push(self):
        self.__stk_list.append(self.__val)
        print(self.__stk_list)
    def pop(self):
        del(self.__stk_list[0])
        print(self.__stk_list)

class stack_counter(stack):
    def __init__(self, counter=0):
        super().__init__(int(input("choose a number: ")))
        self.__counter = counter
    def pop(self):
        super().pop()
        self.__counter += 1
        print(self.__counter)

stack = stack_counter()
stack.push()
stack.pop()