from LinkedList import LinkedList

if __name__ == '__main__':
    list1 = LinkedList()
    list1.join("a")
    list1.join("c")
    list1.join("b")
    list1.join("a")
    list1.join("a")
    list1.join("c")
    join_string = list1.join("d")

    print("===========Print join returns ==========")
    print(join_string)
    print("=========== Remove duplicates ==========")
    print(list1.remove_duplicate())
    print("=========== Vowels count ==========")
    print(list1.count_vowels())
