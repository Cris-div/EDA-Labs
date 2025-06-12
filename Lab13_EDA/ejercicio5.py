class MaxHeap:
    # 🦁 MaxHeap data structure using a list
    def __init__(self):
        self.heap = []  # Initialize the heap as an empty list

    def insert(self, value):
        # Insert a new value into the heap
        self.heap.append(value)  # Add the value at the end of the list
        self._heapify_up(len(self.heap) - 1)  # Restore heap property by moving it up

    def _heapify_up(self, index):
        # Restore the max-heap property by moving the value up
        parent = (index - 1) // 2  # Get the parent's index
        while index > 0 and self.heap[index] > self.heap[parent]:
            # Swap if current value is greater than its parent
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            index = parent  # Move up to the parent's index
            parent = (index - 1) // 2  # Update the parent index

    def delete_max(self):
        # Remove and return the maximum value (the root of the heap)
        if not self.heap:
            return None  # If heap is empty, return None
        if len(self.heap) == 1:
            return self.heap.pop()  # If only one element, remove and return it

        max_val = self.heap[0]  # Store the root value to return later
        self.heap[0] = self.heap.pop()  # Replace root with the last element
        self._heapify_down(0)  # Restore heap property by moving down the new root
        return max_val  # Return the original max value

    def _heapify_down(self, index):
        # Restore the max-heap property by moving the value down
        length = len(self.heap)
        while True:
            largest = index  # Assume current index is the largest
            left = 2 * index + 1  # Left child index
            right = 2 * index + 2  # Right child index

            if left < length and self.heap[left] > self.heap[largest]:
                largest = left  # Update largest if left child is bigger
            if right < length and self.heap[right] > self.heap[largest]:
                largest = right  # Update largest if right child is bigger

            if largest == index:
                break  # Heap property is satisfied

            # Swap current value with the larger child
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            index = largest  # Move down to the new position


# 🧪 Test cases
def test_max_heap():
    h = MaxHeap()
    h.insert(1);         print("🦁 Test 1:", h.heap==[1])
    for v in [3,2,8,5]:
        h.insert(v)
    print("🦁 Test 2:", h.heap[0]==max(h.heap))
    h.delete_max();      print("🦁 Test 3:", h.heap[0]==max(h.heap))
    h = MaxHeap()
    for v in [5,3,1]:
        h.insert(v)
    h.delete_max();      print("🦁 Test 4:", h.heap==[3,1])
    h=MaxHeap(); h.insert(10)
    print("🦁 Test 5:", h.delete_max()==10 and h.heap==[])

test_max_heap()
