# List to store test results
test_results = []

# Function to record test outcomes using emojis
def record_test(test_name, condition):
    emoji = "✅" if condition else "❌"
    test_results.append(f"{emoji} {test_name}")

# MinHeap class with insertion and heapify-up functionality
class MinHeap:
    def __init__(self):
        # Initialize an empty heap list
        self.heap = []

    def insert(self, value):
        # Add new value to the end of the heap
        self.heap.append(value)
        # Restore the heap property by bubbling the value up
        self._heapify_up(len(self.heap) - 1)

    def _heapify_up(self, index):
        # Repeatedly swap the element with its parent if it violates min-heap property
        while index > 0:
            parent_index = self._parent_index(index)
            # If the current value is smaller than its parent, swap them
            if self.heap[index] < self.heap[parent_index]:
                self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
                index = parent_index
            else:
                break  # If no violation, stop

    def _parent_index(self, index):
        # Return the parent index, or -1 if root
        return (index - 1) // 2 if index > 0 else -1

    def size(self):
        # Return the size of the heap
        return len(self.heap)

    def peek(self):
        # Return the smallest element (at the root) without removing it
        return self.heap[0] if self.heap else None

# Function to test heap insert functionality
def test_1_3():
    heap = MinHeap()

    # 1.3.1 Test inserting a single element
    heap.insert(5)
    record_test("1.3.1 Single element insertion", heap.heap == [5])

    # 1.3.2 Test inserting multiple elements
    heap.insert(3)
    heap.insert(8)
    heap.insert(1)
    record_test("1.3.2 Multiple insertions", len(heap.heap) == 4)

    # 1.3.3 Test if peek correctly identifies the minimum
    record_test("1.3.3 Minimum tracking", heap.peek() == 1)

    # 1.3.4 Validate min-heap property for all nodes
    # Each parent must be <= its children
    valid_heap = all(
        heap.heap[i] <= heap.heap[2*i+1] if 2*i+1 < len(heap.heap) else True
        for i in range(len(heap.heap)//2)
    )
    record_test("1.3.4 Heap property validation", valid_heap)

    # 1.3.5 Check if size tracking is accurate
    record_test("1.3.5 Size consistency", heap.size() == 4)

# 🚀 Run the test cases
test_1_3()

# 📋 Print a summary of all test results
for r in test_results:
    print(r)
