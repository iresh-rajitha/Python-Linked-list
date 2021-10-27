from Node import Node
import random


class LinkedList:
    def __init__(self):
        self.__head = None
        self.__size = 0

    def join(self, value):
        if self.__size == 0:
            self.__head = Node(value)
        else:
            temp = self.__head
            for i in range(self.__size - 1):
                temp = temp.next_node()
            temp.add_node(Node(value))
        self.__size += 1
        return self.get_string()

    def print_nodes(self):
        temp = self.__head
        if temp is None:
            print("list is empty")
        else:
            for i in range(self.__size):
                temp.print_node()
                temp = temp.next_node()

    def remove(self, n):
        node_to_be_removed = None
        if n > self.__size or n <= 0:
            print("Invalid n value")
        else:
            temp = self.__head
            if n == 1:
                node_to_be_removed = self.__head
                self.__head = node_to_be_removed.next_node()
            else:
                for i in range(n - 2):
                    temp = temp.next_node()
                # before_node = temp
                node_to_be_removed = temp.next_node()
                temp.set_next_node(temp.next_node().next_node())
            self.__size -= 1

    def remove_duplicate(self):
        pointer = self.__head
        while pointer is not None:
            letter = pointer.get_value()
            remove_id = self.get_next_element_by_id(letter)
            if remove_id != 0:
                self.remove(remove_id)
            pointer = pointer.next_node()
        return self.get_string()

    def get_next_element_by_id(self, s):
        is_first = True
        temp = self.__head
        for i in range(self.__size):
            if s == temp.get_value():
                if is_first:
                    is_first = False
                else:
                    return i + 1
            temp = temp.next_node()
        return 0

    def get_string(self):
        string = ""
        temp = self.__head
        string += temp.get_value()
        for i in range(self.__size - 1):
            temp = temp.next_node()
            string += temp.get_value()
        return string

    def count_vowels(self):
        count = 0
        temp = self.__head
        for i in range(self.__size - 1):
            if temp.get_value() == "a" or \
                    temp.get_value() == "e" or \
                    temp.get_value() == "i" or \
                    temp.get_value() == "o" or \
                    temp.get_value() == "u":
                count += 1
            temp = temp.next_node()
        return count
