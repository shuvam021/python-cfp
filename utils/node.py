from typing import Any


class Node:
    def __init__(self, data: Any = None, next=None) -> None:
        self.data: Any = data
        self.next: Node = next

    def __repr__(self):
        return f"Node({self.data})"
