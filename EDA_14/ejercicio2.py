# List to store the results of the test cases
test_results = []

# Function to record test outcomes with emoji indicators
def record_test(test_name, condition):
    emoji = "✅" if condition else "❌"
    test_results.append(f"{emoji} {test_name}")

# MinHeap class definition
class MinHeap:
    def __init__(self):
        # Initialize the heap as an empty list
        self.heap = []

    def _parent_index(self, index):
        # Returns the index of the parent node
        # Root (index 0) has no parent, so return -1
        if index == 0:
            return -1
        return (index - 1) // 2

    def _left_child_index(self, index):
        # Returns the index of the left child of a node
        return 2 * index + 1

    def _right_child_index(self, index):
        # Returns the index of the right child of a node
        return 2 * index + 2

    def _has_left_child(self, index):
        # Returns True if the node at 'index' has a left child
        left_index = self._left_child_index(index)
        return left_index < len(self.heap)

    def _has_right_child(self, index):
        # Returns True if the node at 'index' has a right child
        right_index = self._right_child_index(index)
        return right_index < len(self.heap)

# Test suite for index calculations and boundary checks
def test_1_2():
    heap = MinHeap()
    heap.heap = [1, 3, 2, 7, 4, 5, 8]  # Sample heap array for testing

    # 1.2.1 Test: Parent of index 4 should be at index 1
    record_test("1.2.1 Parent calculation", heap._parent_index(4) == 1)

    # 1.2.2 Test: Left and right children of index 1 should be at indices 3 and 4
    left_correct = heap._left_child_index(1) == 3
    right_correct = heap._right_child_index(1) == 4
    record_test("1.2.2 Children calculation", left_correct and right_correct)

    # 1.2.3 Test: Edge case for root node (index 0) should return -1
    record_test("1.2.3 Root node edge case", heap._parent_index(0) == -1 or heap._parent_index(0) is None)

    # 1.2.4 Test: Node at index 1 should have both children
    has_children = heap._has_left_child(1) and heap._has_right_child(1)
    record_test("1.2.4 Boundary validation", has_children)

    # 1.2.5 Test: Node at index 6 should not have children (it's a leaf)
    no_children = not heap._has_left_child(6) and not heap._has_right_child(6)
    record_test("1.2.5 Invalid index handling", no_children)

# 🚀 Run the defined test cases
test_1_2()

# 📋 Print the summary of test results
for r in test_results:
    print(r)
