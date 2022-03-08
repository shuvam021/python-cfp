from abc import ABC, abstractmethod
from typing import Any


class ABCOrderedLinkedList(ABC):

    @abstractmethod
    def add(self, item: Any) -> None:
        """add a new item to the list. Assume the item not already in the list.

        Args:
            item (Any):
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
    def index(self, item: Any) -> int:
        """Assume the item is in the list

        Args:
            item (Any):

        Returns:
            int: position of the item
        """
        pass

    @abstractmethod
    def pop(self) -> Any:
        """Remove and returns the last item in the list.
        Assume the list has at least one item

        Returns:
            Any:
        """
        pass
