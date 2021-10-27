from Node import Node


class LinkedList:
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__size = 0

    def join(self, value):
        new_node = Node(value)
        if self.__size == 0:
            self.__head = new_node
            self.__tail = new_node
        else:
            temp = self.__head
            for i in range(self.__size - 1):
                temp = temp.next_node()
            temp.add_next_node(new_node)
            new_node.set_last_node(temp)
            self.__tail = new_node
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

    def get_first(self):
        if self.__size > 0 :
            return self.__head
        else:
            return None

    def get_last(self):
        if self.__size>0:
            return self.__tail
        else:
            return None

    def contain(self, e):
        temp = self.__head
        for i in range(self.__size):
            if e == str(temp.get_value()):
                return True
            temp=temp.next_node()
        return False

    def add_after(self, n , e):
        new_node = Node(e)

        if n == 0 or n > self.__size :
            print("invalid id")
        elif self.__size == n:
            # self.__tail.print_node()
            self.__tail.set_next_node(new_node)
            new_node.set_last_node(self.__tail)
            self.__tail = new_node
            self.__size += 1
        else:
            temp = self.__head
            for i in range(n-1):
                temp= temp.next_node()
            # temp.print_node()
            new_node.set_last_node(temp)
            new_node.set_next_node(temp.next_node())
            temp.next_node().set_last_node(new_node)
            temp.set_next_node(new_node)
            self.__size += 1
            # temp.next_node(new_node)

    def add_before(self, n , e):
        new_node = Node(e)

        if n == 0 or n > self.__size :
            print("invalid id")
        elif n == 1:
            # self.__tail.print_node()
            self.__head.set_last_node(new_node)
            new_node.set_next_node(self.__head)
            self.__head = new_node
            self.__size += 1
        else:
            temp = self.__head
            for i in range(n-1):
                temp= temp.next_node()
            temp = temp.last_node()
            # temp.print_node()
            new_node.set_last_node(temp)
            new_node.set_next_node(temp.next_node())
            temp.next_node().set_last_node(new_node)
            temp.set_next_node(new_node)
            self.__size += 1
            # temp.next_node(new_node)