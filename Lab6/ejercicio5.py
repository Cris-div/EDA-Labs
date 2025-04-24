class CircularBuffer:
    """Circular buffer for streaming data."""

    def __init__(self, capacity):
        """Initialize an empty buffer with fixed capacity."""
        self.capacity = capacity
        self.buffer = [None] * capacity
        self.write_index = 0
        self.count = 0

    def is_empty(self):
        """Check if buffer is empty."""
        return self.count == 0

    def is_full(self):
        """Check if buffer is full."""
        return self.count == self.capacity

    def add(self, item):
        """Add an item to the buffer, overwriting oldest item if full."""
        self.buffer[self.write_index] = item

        # Move write pointer circularly
        self.write_index = (self.write_index + 1) % self.capacity

        # Update count (up to capacity)
        if self.count < self.capacity:
            self.count += 1

    def get_latest(self, n=1):
        """Get the n most recent items (n <= capacity)."""
        if self.is_empty():
            return []

        n = min(n, self.count)  # Cannot get more items than we have

        result = []
        # Start from the most recent item
        read_index = (self.write_index - 1) % self.capacity

        for _ in range(n):
            result.append(self.buffer[read_index])
            read_index = (read_index - 1) % self.capacity

        return result

    def get_all(self):
        """Get all items in the buffer in order (oldest to newest)."""
        if self.is_empty():
            return []

        result = []
        # Start from the oldest item
        read_index = self.write_index if self.is_full() else 0

        for i in range(self.count):
            result.append(self.buffer[(read_index + i) % self.capacity])

        return result
def test_circular_buffer():
    """Test circular buffer for streaming data."""
    # Create a buffer with capacity 3
    buffer = CircularBuffer(3)

    # Test 1: Initial state
    assert buffer.is_empty() == True, "New buffer should be empty"
    assert buffer.get_all() == [], "Empty buffer should return empty list"

    # Test 2: Adding elements
    buffer.add(1)
    assert buffer.get_all() == [1], "Buffer should contain [1]"

    buffer.add(2)
    assert buffer.get_all() == [1, 2], "Buffer should contain [1, 2]"

    buffer.add(3)
    assert buffer.get_all() == [1, 2, 3], "Buffer should contain [1, 2, 3]"
    assert buffer.is_full() == True, "Buffer should be full"

    # Test 3: Overwriting elements when full
    buffer.add(4)
    assert buffer.get_all() == [2, 3, 4], "Buffer should contain [2, 3, 4]"

    buffer.add(5)
    assert buffer.get_all() == [3, 4, 5], "Buffer should contain [3, 4, 5]"

    # Test 4: Getting latest elements
    assert buffer.get_latest(1) == [5], "Latest 1: [5]"
    assert buffer.get_latest(2) == [5, 4], "Latest 2: [5, 4]"
    assert buffer.get_latest(3) == [5, 4, 3], "Latest 3: [5, 4, 3]"
    assert buffer.get_latest(
        4) == [5, 4, 3], "Latest 4 (limited to capacity): [5, 4, 3]"

    print("Circular buffer tests passed! ✅")
    return True
test_circular_buffer()