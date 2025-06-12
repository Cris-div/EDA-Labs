class MinHeap:
    def __init__(self):
        # Initialize the heap as an empty list
        self.heap = []

    def insert(self, value):
        # Insert a new value into the heap
        self.heap.append(value)  # Add the value to the end of the list
        self._heapify_up(len(self.heap) - 1)  # Restore heap property by bubbling up

    def _heapify_up(self, index):
        # Restore the min-heap property by moving the element up
        parent_index = (index - 1) // 2  # Find the parent index
        while index > 0 and self.heap[index] < self.heap[parent_index]:
            # While the current value is smaller than its parent, swap them
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            index = parent_index  # Move up to the parent's index
            parent_index = (index - 1) // 2  # Update the parent index


# 🧪 Test cases
def test_min_heap_insert():
    h = MinHeap()
    h.insert(5); print("🍀 Test 1:", h.heap == [5])
    h.insert(3); print("🍀 Test 2:", h.heap == [3,5])
    h.insert(4); print("🍀 Test 3:", h.heap == [3,5,4])
    h.insert(1); print("🍀 Test 4:", h.heap == [1,3,4,5])
    # 🍀 Test 5: parent ≤ children
    valid = all(
        (h.heap[i] <= h.heap[2*i+1] if 2*i+1 < len(h.heap) else True)
        and (h.heap[i] <= h.heap[2*i+2] if 2*i+2 < len(h.heap) else True)
        for i in range(len(h.heap))
    )
    print("🍀 Test 5:", valid)

test_min_heap_insert()
