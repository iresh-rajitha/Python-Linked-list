from Node import Node
import random


class LinkedList:
    def __init__(self):
        self.__head = None
        self.__size = 0

    def add_node(self, value):
        if self.__size == 0:
            self.__head = Node(value)
        else:
            temp = self.__head
            for i in range(self.__size - 1):
                temp = temp.next_node()
            temp.add_node(Node(value))
        self.__size += 1

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
            # node_to_be_removed.print_node()
            print("Node: " + str(n) +" "+ node_to_be_removed.get_value())
            self.__size -= 1

    def swap_head_tail(self):
        if self.__size > 1:
            tail = head = None
            temp = self.__head
            for i in range(self.__size - 1):
                temp = temp.next_node()
            temp_head = Node(self.__head.get_value())
            head = self.__head
            head.set_value(temp.get_value())
            temp.set_value(temp_head.get_value())
        else:
            print("Size is not enough for swap nodes")

    def random_remove(self):
        if self.__size != 0:
            self.remove(random.randint(1, self.__size))
        else:
            print("List size is 0")
