class Node:
    def __init__(self, value, nxt=None):
        self.value = value
        self.next = nxt

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    # утиліти
    def append(self, value):
        # додає в кінець
        new = Node(value)
        if not self.head:
            self.head = new
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = new

    @classmethod
    def from_iterable(cls, it):
        lst = cls()
        for x in it:
            lst.append(x)
        return lst

    def to_list(self):
        out = []
        cur = self.head
        while cur:
            out.append(cur.value)
            cur = cur.next
        return out

    # 1) реверс списку in-place
    def reverse_inplace(self):
        prev = None
        cur = self.head
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        self.head = prev

    # 2) сортування односпрямованого списку вставками
    def insertion_sort(self):
        dummy = Node(None)  # штучна голова для відсортованої частини
        cur = self.head
        while cur:
            nxt = cur.next
            # знайти місце вставки
            pos = dummy
            while pos.next and pos.next.value < cur.value:
                pos = pos.next
            # вставка cur після pos
            cur.next = pos.next
            pos.next = cur
            cur = nxt
        self.head = dummy.next

# 3) обʼєднання двох відсортованих односпрямованих списків у один відсортований
def merge_sorted_lists(a: SinglyLinkedList, b: SinglyLinkedList) -> SinglyLinkedList:
    dummy = Node(None)
    tail = dummy
    pa, pb = a.head, b.head

    while pa and pb:
        if pa.value <= pb.value:
            tail.next, pa = pa, pa.next
        else:
            tail.next, pb = pb, pb.next
        tail = tail.next

    tail.next = pa if pa else pb
    out = SinglyLinkedList()
    out.head = dummy.next
    return out

# приклад використання
if __name__ == "__main__":
    # створюємо список і реверсуємо
    lst = SinglyLinkedList.from_iterable([5, 1, 4, 2, 3])
    lst.reverse_inplace()
    print("reverse:", lst.to_list())  # очікуємо [3, 2, 4, 1, 5]

    # сортуємо вставками
    lst2 = SinglyLinkedList.from_iterable([7, 2, 9, 1, 5])
    lst2.insertion_sort()
    print("sorted:", lst2.to_list())  # очікуємо [1, 2, 5, 7, 9]

    # обʼєднання двох відсортованих списків
    a = SinglyLinkedList.from_iterable([1, 3, 5, 7])
    b = SinglyLinkedList.from_iterable([2, 2, 4, 6, 8])
    merged = merge_sorted_lists(a, b)
    print("merged:", merged.to_list())  # очікуємо [1, 2, 2, 3, 4, 5, 6, 7, 8]
