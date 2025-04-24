class CircularQueue:
    """Queue implementation using a circular array."""

    def __init__(self, capacity=5):
        """Initialize an empty queue with a fixed capacity."""
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = -1  # Index of front element
        self.rear = -1   # Index of rear element
        self.size_count = 0

    def is_empty(self):
        """Check if the queue is empty."""
        return self.size_count == 0

    def is_full(self):
        """Check if the queue is full."""
        return self.size_count == self.capacity

    def enqueue(self, item):
        """Add an item to the rear of the queue."""
        if self.is_full():
            raise IndexError("Queue is full! 💥")

        # If queue is empty, set front to 0
        if self.is_empty():
            self.front = 0
            self.rear = 0
        else:
            # Move rear circularly
            self.rear = (self.rear + 1) % self.capacity

        self.queue[self.rear] = item
        self.size_count += 1

    def dequeue(self):
        """Remove and return the front item."""
        if self.is_empty():
            raise IndexError("Queue is empty! 🚫")

        item = self.queue[self.front]
        self.queue[self.front] = None  # Clear reference

        # If this is the last item
        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            # Move front circularly
            self.front = (self.front + 1) % self.capacity

        self.size_count -= 1
        return item

    def peek(self):
        """Return the front item without removing it."""
        if self.is_empty():
            raise IndexError("Queue is empty! 🚫")
        return self.queue[self.front]

    def size(self):
        """Return the number of items in the queue."""
        return self.size_count

    def display(self):
        """Display the queue elements for debugging."""
        if self.is_empty():
            return "Queue: []"

        result = []
        index = self.front
        for _ in range(self.size_count):
            result.append(str(self.queue[index]))
            index = (index + 1) % self.capacity

        return f"Queue: [{', '.join(result)}]"


def rotate_array(nums, k):
    """Rotate array to the right by k steps using circular queue."""
    if not nums or k <= 0:
        return nums

    n = len(nums)
    k = k % n  # Handle case where k > n

    # Use a circular queue to handle rotation
    queue = CircularQueue(n)

    # Fill the queue
    for num in nums:
        queue.enqueue(num)

    # Rotate by dequeuing from the end and enqueueing at the beginning
    # This is more efficient than doing k individual rotations
    result = []

    # First, grab the last k elements (which will move to the front)
    # We'll temporarily store them in a separate list
    to_front = []
    for _ in range(n - k):
        result.append(queue.dequeue())

    # The remaining elements go to the front
    while not queue.is_empty():
        to_front.append(queue.dequeue())

    # Combine the two parts: elements to move to front + remaining elements
    return to_front + result

def test_rotate_array():
    """Test array rotation using circular queue."""
    # Test cases
    test_cases = [
        ([1, 2, 3, 4, 5, 6, 7], 3, [5, 6, 7, 1, 2, 3, 4]),
        ([1, 2, 3, 4, 5], 2, [4, 5, 1, 2, 3]),
        ([1], 1, [1]),
        ([1, 2], 3, [2, 1])  # k > length
    ]

    for i, (nums, k, expected) in enumerate(test_cases):
        result = rotate_array(nums, k)
        assert result == expected, f"Test case {i}: Expected {expected}, got {result}"

    print("All array rotation tests passed! ✅")
    return True

test_rotate_array()