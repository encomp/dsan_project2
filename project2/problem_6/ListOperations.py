from project2.collections.DoubleLinkedList import DoubleLinkedList


def union(llist_1, llist_2):
    union_list = DoubleLinkedList()
    if llist_1 is None and llist_2 is None:
        return union_list
    if llist_1 is None or llist_2 is None:
        if llist_1 is None:
            listas = [llist_2]
        else:
            listas = [llist_1]
    else:
        listas = [llist_1, llist_2]
    for lista in listas:
        for item in lista:
            union_list.insert(item)
    return union_list


def intersection(llist_1, llist_2):
    intersection_list = DoubleLinkedList()
    if llist_1 is None or llist_2 is None:
        return intersection_list
    tmp = DoubleLinkedList()
    for item in llist_1:
        tmp.insert(item)
    for item in llist_2:
        if tmp.remove(item):
            intersection_list.insert(item)
    return intersection_list
