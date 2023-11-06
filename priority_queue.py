class PriorityQueue:
    def __init__(self) -> None:
        """
        Initialize an empty priority queue.
        """
        self.queue = []

    def push(self, item):
        """
        Add an item to the priority queue.

        Args:
            item: The item to add to the priority queue.
        """
        self.queue.append(item)
        self.queue = sorted(self.queue)  # Sort the queue after adding the item
    
    def pop(self):
        """
        Remove and return the highest-priority item from the queue.

        Returns:
            The highest-priority item.
        
        Raises:
            IndexError: If the queue is empty.
        """
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            raise IndexError("Queue is empty")

    def is_empty(self):
        """
        Check if the priority queue is empty.

        Returns:
            bool: True if the queue is empty, False otherwise.
        """
        return len(self.queue) == 0
    
    def size(self):
        """
        Get the number of elements in the priority queue.

        Returns:
            int: The number of elements in the queue.
        """
        return len(self.queue)
    
    def __str__(self):
        """
        Get a string representation of the priority queue.
        """
        output = ""
        for s in self.queue:
            output += str(s)
        return output