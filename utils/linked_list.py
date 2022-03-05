from typing import Any

from utils.abstracts import ABCLinkedList
from utils.node import Node


class LinkedList(ABCLinkedList):
    def __init__(self) -> None:
        super().__init__()
        self.head = None

    def get_list(self) -> list:
        super().get_list()
        return self.head

    def print_ll(self) -> list:
        ll_list = []
        node = self.head
        if self.is_empty():
            return ll_list

        while node:
            ll_list.append(node.data)
            node = node.next
        return ll_list

    def add(self, item: Any) -> None:
        super().add(item)
        if not self.search(item):
            self.append_last(item)
        return

    def remove(self, item: Any) -> None:
        super().remove(item)

        if self.is_empty() or not self.search(item):
            raise Exception(f"{item} not exist ro remove")

        if self.index(item) == self.size():
            # if item is at last position
            self.pop()
            return

        if self.index(item) == 0:
            # if item is at first position
            self.head = self.head.next
            return

        node = self.head
        # if item is in the middle
        while node:
            if node.next is not None and node.next.data == item:
                node.next = node.next.next
            node = node.next
        return

    def search(self, item: Any) -> bool:
        super().search(item)
        if item in self.print_ll():
            return True
        return False

    def is_empty(self) -> bool:
        super().is_empty()
        return self.head is None

    def size(self) -> int:
        super().size()
        return len(self.print_ll())

    def append_last(self, item: Any) -> None:
        super().append_last(item)
        if self.is_empty():
            self.head = Node(item)
        else:
            node = self.head
            while node.next:
                node = node.next
            node.next = Node(item)
        return

    def index(self, item: Any) -> int:
        super().index(item)
        if self.is_empty():
            return 0
        for i, v in enumerate(self.print_ll()):
            if v == item:
                return i

    def insert(self, pos: int, item: Any) -> None:
        super().insert(pos, item)
        if self.is_empty():
            print("Warning: LinkedList is empty, inserted at 0th position")
            self.append_last(item)

        if pos is self.size():
            self.append_last(item)
        else:
            count = 0
            node = self.head
            while node:
                count += 1
                if count == pos:
                    node.next = Node(item, node.next)
                node = node.next

    def pop(self) -> Any:
        super().pop()
        node = self.head
        rm_node = None

        if self.is_empty():
            return

        while node:
            if node.next.next is None:
                rm_node = node.next
                node.next = None
            node = node.next
        return rm_node
