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

    def inorder(self, node=None, result=None):
        """📝 Inorder traversal (left, root, right) with parentheses."""
        if result is None:
            result = []
        if node is None:
            node = self.root
        
        if node is None:
            return result
        
        # For operators, we need parentheses around the expression
        if node.value in {"+", "-", "*", "/"}:
            result.append("(")
            if node.left is not None:
                self.inorder(node.left, result)
            result.append(node.value)
            if node.right is not None:
                self.inorder(node.right, result)
            result.append(")")
        else:
            # For operands, just add the value
            result.append(node.value)
        
        return result

    def preorder(self, node=None, result=None):
        """🚀 Preorder traversal (root, left, right) to generate prefix tokens."""
        if result is None:
            result = []
        if node is None:
            node = self.root
    
        if node is None:
            return result
    
        # Visit root first
        result.append(node.value)
        # Then left subtree (only if it exists)
        if node.left is not None:
            self.preorder(node.left, result)
        # Then right subtree (only if it exists)
        if node.right is not None:
            self.preorder(node.right, result)
    
        return result

    def postorder(self, node=None, result=None):
        """🧠 Postorder traversal (left, right, root) to generate postfix tokens."""
        if result is None:
            result = []
        if node is None:
            node = self.root
    
        if node is None:
            return result
    
        # Visit left subtree first (only if it exists)
        if node.left is not None:
            self.postorder(node.left, result)
        # Then right subtree (only if it exists)
        if node.right is not None:
            self.postorder(node.right, result)
        # Finally visit root
        result.append(node.value)
    
        return result

# Helper to build for tests
def build_tree(postfix):
    stack = []
    ops = {"+", "-", "*", "/"}
    for tok in postfix:
        node = Node(tok)
        if tok in ops:
            node.right = stack.pop()
            node.left = stack.pop()
        stack.append(node)
    return stack.pop() if stack else None

# 🧪 Test cases
def test_traversals():
    tree = ExpressionTree()
    tree.build_from_postfix(["2","3","+","4","1","-","*"])
    # Inorder
    infix = tree.inorder()
    print("📝 Test 1 (Infix):", "".join(infix) == "((2+3)*(4-1))")
    # Preorder
    prefix = tree.preorder()
    print("🚀 Test 1 (Prefix):", " ".join(prefix) == "* + 2 3 - 4 1")
    # Postorder
    postfix = tree.postorder()
    print("🧠 Test 1 (Postfix):", " ".join(postfix) == "2 3 + 4 1 - *")
    # Single node "X"
    single = ExpressionTree()
    single.root = Node("X")
    print("🌱 Test 2 (Infix):", single.inorder() == ["X"])
    print("🌱 Test 2 (Prefix):", single.preorder() == ["X"])
    print("🌱 Test 2 (Postfix):", single.postorder() == ["X"])
    # Empty tree
    empty = ExpressionTree()
    print("📭 Test 3 (Infix):", empty.inorder() == [])
    print("📭 Test 3 (Prefix):", empty.preorder() == [])
    print("📭 Test 3 (Postfix):", empty.postorder() == [])
    # Mixed operators (1*(2+3))
    tree2 = ExpressionTree()
    tree2.build_from_postfix(["1","2","3","+","*"])
    print("🔄 Test 4 (Infix):", "".join(tree2.inorder()) == "(1*(2+3))")
    print("🔄 Test 4 (Prefix):", " ".join(tree2.preorder()) == "* 1 + 2 3")
    print("🔄 Test 4 (Postfix):", " ".join(tree2.postorder()) == "1 2 3 + *")
    # Variables (a+(b*c))
    tree3 = ExpressionTree()
    tree3.build_from_postfix(["a","b","c","*","+"])
    print("🔤 Test 5 (Infix):", "".join(tree3.inorder()) == "(a+(b*c))")
    print("🔤 Test 5 (Prefix):", " ".join(tree3.preorder()) == "+ a * b c")
    print("🔤 Test 5 (Postfix):", " ".join(tree3.postorder()) == "a b c * +")

# 🚀 Run tests
test_traversals()
