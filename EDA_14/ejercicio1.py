# Global list to store the test results
test_results = []

# Helper function to record the result of each test
def record_test(test_name, condition):
    # Use a checkmark emoji for a passed test, cross for a failed test
    emoji = "✅" if condition else "❌"
    # Append the formatted result to the results list
    test_results.append(f"{emoji} {test_name}")

# MinHeap class: Basic implementation of a min-heap structure
class MinHeap:
    def __init__(self):
        # Initialize an empty list to represent the heap
        self.heap = []

    def is_empty(self):
        # Return True if the heap has no elements
        return len(self.heap) == 0

    def size(self):
        # Return the number of elements in the heap
        return len(self.heap)

    def peek(self):
        # Return the minimum element (at the top of the heap) without removing it
        # If the heap is empty, return None
        if self.is_empty():
            return None
        return self.heap[0]

# Function to test basic functionalities of the MinHeap class
def test_1_1():
    # 1.1.1 Test if a new heap is initialized as empty
    heap = MinHeap()
    record_test("1.1.1 Empty heap initialization", heap.is_empty() == True)

    # 1.1.2 Simulate adding elements and test size tracking
    heap.heap = [1, 3, 2]  # Direct insertion (not maintaining heap structure, for simplicity)
    record_test("1.1.2 Size tracking", heap.size() == 3)

    # 1.1.3 Test peek functionality (should return the first element)
    record_test("1.1.3 Peek functionality", heap.peek() == 1)

    # 1.1.4 Edge case: peek on an empty heap should return None
    empty_heap = MinHeap()
    record_test("1.1.4 Empty heap edge case", empty_heap.peek() is None)

    # 1.1.5 Test if the result of is_empty is a boolean
    record_test("1.1.5 Type validation", isinstance(heap.is_empty(), bool))

# 🚀 Run all defined tests
test_1_1()

# 📋 Print a summary of all test results
for r in test_results:
    print(r)
