class Node:
    """🔢 Node for an expression tree."""
    def __init__(self, value):
        self.value = value     # Operator (str) or operand (str/number)
        self.left = None       # ↙️ Left child
        self.right = None      # ↘️ Right child
class ExpressionTree:
    def __init__(self):
        self.root = None

    def build_from_postfix(self, postfix_tokens):
        """🔨 Build tree from postfix tokens using a stack."""
        # Your solution here 🛠️
        stack=[]
        for token in postfix_tokens:
            node=Node(token)
            if node.value in ["+","-","*","/"]:
                node.right=stack.pop()
                node.left=stack.pop()
            stack.append(node)
        self.root=stack.pop()if stack else None

class EvaluableExpressionTree(ExpressionTree):
    def __init__(self):
        super().__init__()

    def evaluate(self, node=None):
        """🧮 Evaluate an expression tree containing integers and +,-,*,/."""
        # Your solution here 🛠️
        if node is None:
            node=self.root
        if node.value not in ["+","-","*","/"]:
            return int(node.value)
        lef=self.evaluate(node.left)
        right=self.evaluate(node.right)
        if node.value=="+": return lef + right
        if node.value=="-": return lef - right
        if node.value=="*": return lef * right
        if node.value=="/": return lef / right



# Helper to build and test
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
def test_evaluate_expression_tree():
    # Test 1: Leaf only
    tree = EvaluableExpressionTree()
    tree.root = Node("5")
    print("🌿 Test 1:", tree.evaluate() == 5)

    # Test 2: Addition
    tree = EvaluableExpressionTree()
    tree.build_from_postfix(["2", "3", "+"])
    print("➕ Test 2:", tree.evaluate() == 5)

    # Test 3: Mixed ops ((2+3)*4)
    tree = EvaluableExpressionTree()
    tree.build_from_postfix(["2", "3", "+", "4", "*"])
    print("🔁 Test 3:", tree.evaluate() == 20)

    # Test 4: Division (8/4)
    tree = EvaluableExpressionTree()
    tree.build_from_postfix(["8", "4", "/"])
    print("➗ Test 4:", tree.evaluate() == 2)

    # Test 5: Nested ((10+5)*2)-(8/4)
    tree = EvaluableExpressionTree()
    tree.build_from_postfix(["10", "5", "+", "2", "*", "8", "4", "/", "-"])
    print("🧠 Test 5:", tree.evaluate() == 28)

# 🚀 Run tests
test_evaluate_expression_tree()