class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def merge_sorted(list1, list2):
    if not list1:
        return list2
    if not list2:
        return list1

    if list1.data <= list2.data:
        head = list1
        current1 = list1.next
        current2 = list2
    else:
        head = list2
        current1 = list1
        current2 = list2.next

    current = head

    while current1 and current2:
        if current1.data <= current2.data:
            current.next = current1
            current1 = current1.next
        else:
            current.next = current2
            current2 = current2.next
        current = current.next

    if current1:
        current.next = current1
    elif current2:
        current.next = current2

    return head

list1 = Node(1)
list1.next = Node(3)
list1.next.next = Node(5)

list2 = Node(2)
list2.next = Node(4)
list2.next.next = Node(6)

merged_list = merge_sorted(list1, list2)


current = merged_list
while current:
    print(current.data)
    current = current.next
