class MinHeap:
    def __init__(self):
        # Initialize the heap as an empty list
        self.heap = []

    def delete_min(self):
        # Remove and return the smallest element (root of the heap)
        if not self.heap:
            return None  # Return None if heap is empty

        if len(self.heap) == 1:
            return self.heap.pop()  # Only one element, just pop it

        min_value = self.heap[0]  # Save the minimum value (root)
        self.heap[0] = self.heap.pop()  # Move the last element to root
        self._heapify_down(0)  # Restore heap property by bubbling down
        return min_value  # Return the removed min value

    def _heapify_down(self, index):
        # Restore the min-heap property by moving the element down
        length = len(self.heap)
        while True:
            smallest = index  # Assume current index is smallest
            left = 2 * index + 1  # Left child index
            right = 2 * index + 2  # Right child index

            # Check if left child is smaller
            if left < length and self.heap[left] < self.heap[smallest]:
                smallest = left
            # Check if right child is smaller
            if right < length and self.heap[right] < self.heap[smallest]:
                smallest = right

            if smallest == index:
                break  # Heap property is satisfied

            # Swap with the smallest child
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            index = smallest  # Continue down the tree


# 🧪 Test cases
def test_min_heap_delete_min():
    h = MinHeap()
    print("🧹 Test 1:", h.delete_min() is None)
    h.heap=[1]; print("🧹 Test 2:", h.delete_min()==1 and h.heap==[])
    h.heap=[1,3,2]; print("🧹 Test 3:", h.delete_min()==1 and h.heap==[2,3])
    h.heap=[1,3,4,5]; print("🧹 Test 4:", h.delete_min()==1 and h.heap==[3,5,4])
    h.heap=[1,2,3,4,5]
    print("🧹 Test 5:", h.delete_min()==1)

test_min_heap_delete_min()
