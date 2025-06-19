# List to store test results
test_results = []

# Utility function to record test results using emoji
def record_test(test_name, condition):
    emoji = "✅" if condition else "❌"
    test_results.append(f"{emoji} {test_name}")

# MaxHeap class: stores the largest value at the root
class MaxHeap:
    def __init__(self):
        # Initialize an empty heap list
        self.heap = []

    def insert(self, value):
        # Add a value and restore the max-heap property
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)

    def delete_max(self):
        # Remove and return the maximum element (root of the heap)
        if not self.heap:
            return None
        max_value = self.heap[0]
        last_value = self.heap.pop()  # Remove last element
        if self.heap:
            self.heap[0] = last_value  # Replace root with last element
            self._heapify_down(0)      # Restore heap property
        return max_value

    def build_heap(self, array):
        # Efficiently build a max-heap from an array in O(n) time
        self.heap = array
        for i in range(len(self.heap) // 2 - 1, -1, -1):
            self._heapify_down(i)

    def _heapify_up(self, index):
        # Move the inserted element up the heap to maintain max-heap property
        while index > 0:
            parent_index = (index - 1) // 2
            if self.heap[index] > self.heap[parent_index]:
                self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
                index = parent_index
            else:
                break

    def _heapify_down(self, index):
        # Move the element at index down to its proper position
        while True:
            largest = index
            left = 2 * index + 1
            right = 2 * index + 2

            if left < len(self.heap) and self.heap[left] > self.heap[largest]:
                largest = left
            if right < len(self.heap) and self.heap[right] > self.heap[largest]:
                largest = right

            if largest == index:
                break

            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            index = largest

# Function to test MaxHeap behavior
def test_1_5():
    heap = MaxHeap()

    # 1.5.1 Test inserting values and checking if root is the maximum
    heap.insert(3)
    heap.insert(1)
    heap.insert(5)
    record_test("1.5.1 MaxHeap insertion", heap.heap[0] == 5)

    # 1.5.2 Test removing the max value and checking if it's correct
    max_val = heap.delete_max()
    record_test("1.5.2 MaxHeap deletion", max_val == 5)

    # 1.5.3 Test building a heap from an unsorted array
    heap.build_heap([3, 1, 4, 1, 5, 9, 2])
    record_test("1.5.3 Build heap from array", heap.heap[0] == max(heap.heap))

    # 1.5.4 Verify the max-heap property: parent >= children
    valid_max_heap = all(
        heap.heap[i] >= heap.heap[2*i+1] if 2*i+1 < len(heap.heap) else True
        for i in range(len(heap.heap)//2)
    )
    record_test("1.5.4 Heap property verification", valid_max_heap)

    # 1.5.5 Check handling of empty array
    heap.build_heap([])
    record_test("1.5.5 Empty array handling", len(heap.heap) == 0)

# 🚀 Run the test suite
test_1_5()

# 📋 Print test results summary
for r in test_results:
    print(r)
