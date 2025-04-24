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

        if self.is_empty():
            self.front = 0
            self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.capacity

        self.queue[self.rear] = item
        self.size_count += 1

    def dequeue(self):
        """Remove and return the front item."""
        if self.is_empty():
            raise IndexError("Queue is empty! 🚫")

        item = self.queue[self.front]
        self.queue[self.front] = None  # Clear reference

        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
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

def sliding_window_maximum(nums, k):
    """Find maximum elements in sliding windows of size k."""
    if not nums or k <= 0 or k > len(nums):
        return []

    result = []
    q = CircularQueue(k)

    for i in range(len(nums)):
        # Remove elements outside current window
        while not q.is_empty() and q.peek()[0] < i - k + 1:
            q.dequeue()

        # Remove smaller elements (they won't be maximum)
        while not q.is_empty() and nums[q.peek()[0]] < nums[i]:
            q.dequeue()

        # Add current element
        q.enqueue((i, nums[i]))
        print(f"Paso {i}: Agregado {(i, nums[i])}, Cola → {q.display()}")  # 👈 Aquí ves el estado

        # Add to result if we've processed at least k elements
        if i >= k - 1:
            result.append(nums[q.peek()[0]])

    return result

def test_sliding_window_maximum():
    """Test sliding window maximum algorithm."""
    test_cases = [
        ([1, 3, -1, -3, 5, 3, 6, 7], 3, [3, 3, 5, 5, 6, 7]),
        ([1, 2, 3, 4, 5], 3, [3, 4, 5]),
        ([9, 8, 7, 6, 5], 3, [9, 8, 7]),
        ([1, 1, 1, 1, 1], 3, [1, 1, 1]),
        ([], 3, [])
    ]

    for i, (nums, k, expected) in enumerate(test_cases):
        result = sliding_window_maximum(nums, k)
        assert result == expected, f"Test case {i}: Expected {expected}, got {result}"

    print("All sliding window maximum tests passed! ✅")
    return True

test_sliding_window_maximum()
