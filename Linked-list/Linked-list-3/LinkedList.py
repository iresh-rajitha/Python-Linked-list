from Node import Node
import array


class LinkedList:
    def __init__(self):
        self.__head = None
        self.__size = 0

    def get_size(self):
        return self.__size

    def get_head(self):
        return self.__head

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
        print(self.get_string())

    def get_string(self):
        string = ""
        temp = self.__head
        string += str(temp.get_value()) + "->"
        for i in range(self.__size - 1):
            temp = temp.next_node()
            string += str(temp.get_value()) + "->"
        string += "\b\b"
        return string

    def merge2lists(self, list1, list2):
        full_list = []
        temp = list1.get_head()
        for i in range(list1.get_size()):
            full_list.append(temp.get_value())
            temp = temp.next_node()

        temp = list2.get_head()
        for i in range(list2.get_size()):
            full_list.append(temp.get_value())
            temp = temp.next_node()

        full_list.sort()
        merge_list = LinkedList()
        for x in full_list:
            merge_list.join(x)
        return merge_list
