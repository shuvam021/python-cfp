from abc import ABC, abstractmethod


class ABCStack(ABC):
    """
    Follows Last In First Out(LIFO)
    insertion and deletion happened at end position
    """
    @abstractmethod
    def push(self, item) -> None:
        """Adds a new item to the top of the stack
        :param item:
        """
        pass

    @abstractmethod
    def pop(self) -> object:
        """removes the top item of the stack

        :rtype: object (removed object)
        """
        pass

    @abstractmethod
    def peek(self) -> object:
        """returns the top item of the stack but does not remove it

        :rtype: object (removed object)
        """
        pass

    @abstractmethod
    def is_empty(self) -> bool:
        """tests to see whether the stack is empty

        :rtype: bool
        """
        pass

    @abstractmethod
    def size(self) -> int:
        """Returns numbers of items on the stack

        :rtype: bool
        """
        pass
