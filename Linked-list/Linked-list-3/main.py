from LinkedList import LinkedList

if __name__ == '__main__':
    list1 = LinkedList()
    list1.join(2)
    list1.join(11)
    list1.join(19)
    list1.join(21)
    list1.join(23)
    list1.join(24)
    print("===== List 1 =======")
    list1.print_nodes()

    list2 = LinkedList()
    list2.join(3)
    list2.join(9)
    list2.join(15)
    list2.join(16)
    list2.join(22)
    print("===== List 2 =======")
    list2.print_nodes()

    print("===== Merge List =======")
    merged_list = list1.merge2lists(list1, list2)
    merged_list.print_nodes()
