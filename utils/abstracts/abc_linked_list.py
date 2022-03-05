from abc import ABC, abstractmethod
from typing import Any


class ABCLinkedList(ABC):
    """
    A linked list is a linear collection of data elements whose order is not determined by the placement in memory.
    Instead, each element is stored in a node which points to the next node.
    """

    @abstractmethod
    def add(self, item: Any) -> None:
        """add a new item to the list. Assume the item not already in the list.

        Args:
            item (Any): _description_
        """
        pass

    @abstractmethod
    def remove(self, item: Any) -> None:
        """Removes the item from the list.
        Assume the item present in the list

        Args:
            item (Any): possible item to remove this linked list.
        """
        pass

    @abstractmethod
    def search(self, item: Any) -> bool:
        """Search for the item in the list.

        Args:
            item (Any): possible item to search for in this linked list.
        Returns:
            bool
        """
        pass

    @abstractmethod
    def is_empty(self) -> bool:
        """Tests to see whether the linked list is empty.

        Returns:
            bool
        """
        pass

    @abstractmethod
    def size(self) -> int:
        """Tests to see size of list linked list.

        Returns:
            int
        """
        pass

    @abstractmethod
    def append_last(self, item: Any) -> None:
        """Adds a new item to the end of the list making it the last item in the collection.
        Assume the the item not already in the list.

        Args:
            item (Any): possible item to maintain this linked list.
        Returns:
            None
        """
        pass

    @abstractmethod
    def index(self, item: Any) -> int:
        """Asume the item is in the list

        Args:
            item (Any): _description_

        Returns:
            int: position of the item
        """
        pass

    @abstractmethod
    def insert(self, pos: int, item: Any) -> None:
        """Adds a new item to the list at position. Assume the item is not in the list and there are enough existing items to have position pos.

        Args:
            pos (int): _description_
            item (Any): _description_
        """
        pass

    @abstractmethod
    def pop(self) -> Any:
        """Remove and returns the last item in the list.
        Assume the list has at least one item

        Returns:
            Any: _description_
        """
        pass
