from abc import ABC, abstractmethod


class ABCQueue(ABC):
    """
    Queue follows First In First Out(FIFO)
    insertion(enqueue) happened at end position
    deletion(dequeue) happened at first position
    """

    @abstractmethod
    def enqueue(self, item) -> None:
        """Adds a new item to the rear of the queue"""
        pass

    @abstractmethod
    def dequeue(self) -> object:
        """Removes the front item from the queue
        :rtype: object (Removed object)
        """
        pass

    @abstractmethod
    def is_empty(self) -> bool:
        """tests to see whether the queue is empty

        :rtype: bool
        """
        pass

    @abstractmethod
    def size(self) -> int:
        """Returns numbers of items in the queue

        :rtype: bool
        """
        pass
