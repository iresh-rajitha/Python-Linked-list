from LinkedList import LinkedList

if __name__ == '__main__':
    # print("hello")
    l = LinkedList()
    l.join("Iresh")
    l.join("Rajitha")
    l.join("Kalhara")
    # l.print_nodes()
    print("========== get first element ========")
    l.get_first().print_node()
    print("========== get first element =========")
    l.get_last().print_node()
    print("========== is contain ======")
    print(l.contain("Iresh"))
    print(l.contain("Rajitha"))
    print(l.contain("Kalhara"))
    print(l.contain("Kalh"))
    print("========== full list before add new elements   ======")
    l.print_nodes()
    print("========== add III after 1   ======")
    l.add_after(1,"III")
    l.print_nodes()
    print("========== add rrr  before 4  ======")
    l.add_before(4,"rrr")
    l.print_nodes()