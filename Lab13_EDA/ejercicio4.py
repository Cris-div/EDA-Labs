class MinHeap:
    def __init__(self):
        # Initialize an empty heap list
        self.heap = []

    def build_heap(self, array):
        # Transform an unordered array into a valid min-heap
        self.heap = array[:]  # Copy the array into the heap
        # Start from the last parent node down to the root
        for i in reversed(range(len(self.heap) // 2)):
            self._heapify_down(i)  # Restore heap property from this index

    def _heapify_down(self, index):
        # Restore the min-heap property by pushing element down the tree
        length = len(self.heap)
        while True:
            smallest = index  # Assume current index is the smallest
            left = 2 * index + 1  # Calculate left child index
            right = 2 * index + 2  # Calculate right child index

            # Check if left child is smaller than current smallest
            if left < length and self.heap[left] < self.heap[smallest]:
                smallest = left

            # Check if right child is smaller than the current smallest
            if right < length and self.heap[right] < self.heap[smallest]:
                smallest = right

            if smallest == index:
                break  # Heap property is satisfied, stop the loop

            # Swap current with the smallest child
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            index = smallest  # Move to the next index to continue heapifying


# 🧪 Test cases
def test_build_heap():
    h = MinHeap()
    h.build_heap([5,3,8,1,2]); print("🔨 Test 1:", h.heap[0]==1)
    h.build_heap([7,6,5,4,3,2,1]); print("🔨 Test 2:", h.heap[0]==1)
    h.build_heap([2,1]);           print("🔨 Test 3:", h.heap==[1,2])
    h.build_heap([10]);            print("🔨 Test 4:", h.heap==[10])
    h.build_heap([]);              print("🔨 Test 5:", h.heap==[])

test_build_heap()
