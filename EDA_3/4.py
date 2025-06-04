class ExprNode:
    """🔢 Node for an expression tree."""
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
    def is_operator(self):
        return self.value in ['+', '-', '*', '/']

class ExpressionTree:
    """📝 Binary tree for building and traversing expressions."""
    def __init__(self):
        self.root = None  # 🌱 Root of the expression tree

    def infix_traversal(self, node=None):
        """
        📝 Return a string of the infix expression with parentheses.
        """
        # Your solution here 🛠️
        if node is None:
            node=self.root
        if node is None:
            return ""
        if node.value not in ["+","-","*","/"]:
            return str(node.value)
        left_infix=self.infix_traversal(node.left)
        right_infex=self.infix_traversal(node.right)
        return f"({left_infix} {node.value} {right_infex})"

# 🧪 Test cases
def test_infix_traversal():
    tree = ExpressionTree()
    # Test 1: Empty tree
    print("📝 Test 1:", tree.infix_traversal() == "")
    # Build (2 + 3)
    root = ExprNode("+")
    root.left = ExprNode("2")
    root.right = ExprNode("3")
    tree.root = root
    print("📝 Test 2:", tree.infix_traversal() == "(2 + 3)")
    # Build ((2+3)*4)
    root = ExprNode("*")
    left = ExprNode("+"); left.left = ExprNode("2"); left.right = ExprNode("3")
    root.left = left; root.right = ExprNode("4")
    tree.root = root
    print("📝 Test 3:", tree.infix_traversal() == "((2 + 3) * 4)")
    # Build ((1*2) - (8/4))
    root = ExprNode("-")
    l = ExprNode("*"); l.left = ExprNode("1"); l.right = ExprNode("2")
    r = ExprNode("/"); r.left = ExprNode("8"); r.right = ExprNode("4")
    root.left = l; root.right = r
    tree.root = root
    print("📝 Test 4:", tree.infix_traversal() == "((1 * 2) - (8 / 4))")
    # Test 5: Single operand
    tree.root = ExprNode("X")
    print("📝 Test 5:", tree.infix_traversal() == "X")

# 🚀 Run tests
test_infix_traversal()