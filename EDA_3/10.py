class Node:
    """🔢 Node for an expression tree."""
    def __init__(self, value):
        self.value = value     # Operator (str) or operand (str/number)
        self.left = None       # ↙️ Left child
        self.right = None      # ↘️ Right child
class ExpressionTree:
    """🌳 Expression tree with build and traversal placeholders."""
    def __init__(self):
        self.root = None

    def build_from_postfix(self, postfix_tokens):
        """🔨 Build tree from postfix tokens."""
        stack = []
        ops = {"+", "-", "*", "/"}
        for tok in postfix_tokens:
            node = Node(tok)
            if tok in ops:
                node.right = stack.pop()
                node.left = stack.pop()
            stack.append(node)
        self.root = stack.pop() if stack else None

class EvaluableExpressionTree(ExpressionTree):
    def __init__(self):
        super().__init__()

    def simplify(self, node=None):
        """
        🔄 Simplify constant-only subtrees into single numeric leaves.
        """
        # Your solution here 🛠️
        if node is None:
            node=self.root
        if node is None:
            return 
        if node.value not in ["+","-","*","/"]:
            return node
        node.left=self.simplify(node.left)
        node.right=self.simplify(node.right)
        if (node.left.value not in ["+","-","*","/"]  and node.left.value.isdigit() and
            node.right.value not in ["+","-","*","/"] and node.right.value.isdigit()):
            left = int(node.left.value)
            right = int(node.right.value)
            if node.value == "+": return Node(str(left + right))
            if node.value == "-": return Node(str(left - right))
            if node.value == "*": return Node(str(left * right))
            if node.value == "/": return Node(str(left // right))
        return node

# Helper to build and test (reuse from previous challenge)
def build_tree(postfix):
    stack = []
    ops = {"+", "-", "*", "/"}
    for tok in postfix:
        node = Node(tok)
        if tok in ops:
            node.right = stack.pop()
            node.left  = stack.pop()
        stack.append(node)
    return stack.pop() if stack else None

# 🧪 Test cases
def test_simplify_expression_tree():
    et = EvaluableExpressionTree()

    # Test 1: All constants (2+3)
    et.root = build_tree(["2", "3", "+"])
    simp = et.simplify()
    print("🔢 Test 1:", simp and simp.value == "5" and simp.left is None and simp.right is None)

    # Test 2: Mixed (x+3)
    et.root = build_tree(["x", "3", "+"])
    simp = et.simplify()
    cond2 = (simp and simp.value == "+" and simp.left.value == "x" and simp.right.value == "3")
    print("🔤 Test 2:", cond2)

    # Test 3: Nested constants ((2*3)+(8-3))
    et.root = build_tree(["2", "3", "*", "8", "3", "-", "+"])
    simp = et.simplify()
    print("🎯 Test 3:", simp and simp.value == "11" and simp.left is None and simp.right is None)

    # Test 4: Partial ((2+3)*(z*4))
    et.root = build_tree(["2", "3", "+", "z", "4", "*", "*"])
    simp = et.simplify()
    cond4 = (simp and simp.value == "*" and simp.left.value == "5" and simp.right.value == "*")
    print("🔄 Test 4:", cond4)

    # Test 5: No simplify (x*y)
    et.root = build_tree(["x", "y", "*"])
    simp = et.simplify()
    print("🌿 Test 5:", simp and simp.value == "*" and simp.left.value == "x" and simp.right.value == "y")

# 🚀 Run tests
test_simplify_expression_tree()