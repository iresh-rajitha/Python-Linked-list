class Node:

    def __init__(self, value):
        self.__value = value
        self.__next = None
        self.__prev = None

    def next_node(self):
        return self.__next

    def last_node(self):
        return self.__prev

    def add_node(self, new_node): # need to change
        self.__next = new_node

    def add_next_node(self, node):
        self.__next= node

    def print_node(self):
        print(str(self.__value))

    def set_next_node(self, node):
        self.__next = node

    def set_last_node(self, node):
        self.__prev = node

    def set_value(self, value):
        self.__value = value

    def get_value(self):
        return self.__value
