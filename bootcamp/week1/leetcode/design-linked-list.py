# solved with doubly linked list
# improved deleteAtTail -> T.C. O(1)

class ListNode:
    def __init__(self, val, left_node=None, right_node=None):
        self.val = val
        self.prev = left_node
        self.next = right_node


class MyLinkedList(object):
    def __init__(self):
        self.left = ListNode(-1)  # dummy head
        self.right = ListNode(-1)  # dummy tail

        # initiate the dummy linking
        self.left.next = self.right
        self.right.prev = self.left

        self.size = 0

    def get(self, index):
        # handling edge case
        if index < 0 or index >= self.size:
            return -1

        curr = self.left.next
        for _ in range(index):
            curr = curr.next
        return curr.val

    def addAtHead(self, val):
        self.addAtIndex(0, val)

    def addAtTail(self, val):
        # addAtIndex(self.size, val) was taking O(n)
        # Optimization: adding at tail is now O(1)
        curr_right = self.right  # tail node
        curr_left = curr_right.prev

        self.__insertNode(left=curr_left, val=val, right=curr_right)

    def addAtIndex(self, index, val):
        if index > self.size:
            return

        if index == self.size:  # if we want to add right before the dummy tail
            self.addAtTail(val)
        else:
            curr_left = self.left  # head node
            for _ in range(index):
                curr_left = curr_left.next

            curr_right = curr_left.next

            self.__insertNode(left=curr_left, val=val, right=curr_right)

    def __insertNode(self, left, val, right):
        # create a new_node and link with the current left and right
        new_node = ListNode(val, left_node=left, right_node=right)

        # now update our curr_left and curr_right nodes with the new_node
        left.next = new_node
        right.prev = new_node

        # increment the size
        self.size += 1

    def deleteAtHead(self):
        self.deleteAtIndex(0)

    def deleteAtTail(self):
        # deletion in O(1) time
        # initialization
        node_to_delete = self.right.prev
        next_left = node_to_delete.prev

        self.__deleteNode(
            left=next_left,
            node=node_to_delete,
            right=self.right  # tail node
        )

    def deleteAtIndex(self, index):
        if index < 0 or index >= self.size:
            return

        if index == self.size - 1:  # want to delete right before the dummy tail
            self.deleteAtTail()
        else:
            # same as insertion
            curr_left = self.left
            for _ in range(index):
                curr_left = curr_left.next

            # initialization
            node_to_delete = curr_left.next
            next_right = node_to_delete.next

            self.__deleteNode(
                left=curr_left,
                node=node_to_delete,
                right=next_right
            )

    def __deleteNode(self, left, node, right):
        # swap the link
        left.next = right
        right.prev = left

        # cleanup orphan node
        node.prev = None
        node.next = None
        del node

        # decrement the size
        self.size -= 1