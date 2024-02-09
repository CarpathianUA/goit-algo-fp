class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node

    @staticmethod
    def insert_after(prev_node: Node, data):
        if prev_node is None:
            print("Попереднього вузла не існує.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def insert_before(self, next_node: Node, data):
        if next_node is None:
            print("Наступного вузла не існує.")
            return

        new_node = Node(data)

        if next_node is self.head:
            new_node.next = self.head
            self.head = new_node
            return

        current = self.head
        while current and current.next != next_node:
            current = current.next
        current.next = new_node
        new_node.next = next_node

    def delete_node(self, key: int):
        cur = self.head
        if cur and cur.data == key:
            self.head = cur.next
            return
        prev = None
        while cur and cur.data != key:
            prev = cur
            cur = cur.next
        if cur is None:
            return
        prev.next = cur.next

    def search_element(self, data: int) -> Node | None:
        cur = self.head
        while cur:
            if cur.data == data:
                return cur
            cur = cur.next
        return None

    def print_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

    def reverse_list(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    @staticmethod
    def get_middle(head):
        if not head:
            return head

        slow = head
        fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        return slow

    def merge_sorted_lists(self, left, right):
        if not left:
            return right
        if not right:
            return left

        if left.data <= right.data:
            result = left
            result.next = self.merge_sorted_lists(left.next, right)
        else:
            result = right
            result.next = self.merge_sorted_lists(left, right.next)

        return result

    def merge_sort(self, head):
        if not head or not head.next:
            return head

        middle = self.get_middle(head)
        next_to_middle = middle.next

        middle.next = None

        left = self.merge_sort(head)
        right = self.merge_sort(next_to_middle)

        sorted_list = self.merge_sorted_lists(left, right)

        return sorted_list

    def sort(self):
        self.head = self.merge_sort(self.head)


# function to merge two sorted linked lists
def merge_sorted_linked_lists(list1, list2):
    dummy = Node(0)
    tail = dummy
    head1 = list1.head
    head2 = list2.head

    while head1 and head2:
        if head1.data < head2.data:
            tail.next = head1
            head1 = head1.next
        else:
            tail.next = head2
            head2 = head2.next
        tail = tail.next

    tail.next = head1 or head2

    return dummy.next


if __name__ == "__main__":
    llist = LinkedList()

    llist.insert_at_beginning(5)
    llist.insert_at_beginning(10)
    llist.insert_at_beginning(15)

    llist.insert_at_end(20)
    llist.insert_at_end(25)

    prev_node = llist.search_element(10)
    llist.insert_after(prev_node, 11)

    next_node = llist.search_element(20)
    llist.insert_before(next_node, 19)

    print("Linked list:")
    llist.print_list()

    print("Reversed linked list:")
    llist.reverse_list()
    llist.print_list()

    print("Sorted linked list (merge sort):")
    llist.sort()
    llist.print_list()

    # merge two sorted linked lists
    llist1 = LinkedList()
    llist1.insert_at_beginning(55)
    llist1.insert_at_beginning(101)
    llist1.insert_at_beginning(159)

    llist1.insert_at_end(202)
    llist1.insert_at_end(253)
    llist1.sort()

    merged_head = merge_sorted_linked_lists(llist, llist1)
    merged_list = LinkedList()
    merged_list.head = merged_head
    print("Merged linked list:")
    merged_list.print_list()
