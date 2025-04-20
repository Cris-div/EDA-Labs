class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedQueue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size_count = 0

    def is_empty(self):
        return self.front is None

    def enqueue(self, item):
        new_node = Node(item)
        if self.is_empty():
            self.front = new_node
        else:
            self.rear.next = new_node
        self.rear = new_node
        self.size_count += 1
        return True

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty! 🚫")
        item = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        self.size_count -= 1
        return item

    def peek(self):
        if self.is_empty():
            raise IndexError("Queue is empty! 🚫")
        return self.front.data

    def size(self):
        return self.size_count

    def __str__(self):
        if self.is_empty():
            return "Queue: []"
        result = []
        current = self.front
        while current:
            result.append(str(current.data))
            current = current.next
        return f"Queue: [{', '.join(result)}]"

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def level_order_traversal(root):
    if not root:
        return []
    result = []
    queue = LinkedQueue()
    queue.enqueue(root)
    while not queue.is_empty():
        node = queue.dequeue()
        result.append(node.value)
        if node.left:
            queue.enqueue(node.left)
        if node.right:
            queue.enqueue(node.right)
    return result


def test_level_order_traversal():
    root=TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)

    print("Binary Tree Structure:")
    print("       1")
    print("     /   \\")
    print("    2     3")
    print("   / \\   / \\")
    print("  4   5 6   7")

    # Perform level-order traversal
    traversal = level_order_traversal(root)

    print("\nLevel-order traversal result:")
    print(" -> ".join(map(str, traversal)))

    # Verify the result
    expected = [1, 2, 3, 4, 5, 6, 7]
    print(f"Expected: {expected}")
    print(f"Traversal correct: {traversal == expected} ✅")

test_level_order_traversal()

