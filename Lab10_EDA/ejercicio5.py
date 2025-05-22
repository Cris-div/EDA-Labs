class Node:
    """Node for expression tree"""
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def is_operator(self):
        return self.value in ('+', '-', '*', '/')

def simplify_expression_tree(root):
    """Simplify expression tree by evaluating constant subtrees"""
    if root is None:
        return None

    # Simplify subtrees recursively
    root.left = simplify_expression_tree(root.left)
    root.right = simplify_expression_tree(root.right)

    if root.is_operator():
        # Try to evaluate constant subtrees
        if (root.left and not root.left.is_operator() and
            root.right and not root.right.is_operator()):
            try:
                left_val = float(root.left.value)
                right_val = float(root.right.value)

                # Evaluate the operation
                if root.value == '+':
                    result = left_val + right_val
                elif root.value == '-':
                    result = left_val - right_val
                elif root.value == '*':
                    result = left_val * right_val
                elif root.value == '/':
                    if right_val != 0:
                        result = left_val / right_val
                    else:
                        return root  # Keep as is if division by zero

                # Create a new node with the result
                result_value = str(int(result) if result == int(result) else result)
                return Node(result_value)

            except ValueError:
                # If either side is not a number, cannot simplify
                return root
    return root


# ✅ Test cases
# Test 1: All constants
# Tree:    +        Result: 5
#         / \
#        2   3
node1 = Node('+')
node1.left = Node('2')
node1.right = Node('3')
result1 = simplify_expression_tree(node1)
print(result1.value == '5' and result1.left is None and result1.right is None)  # 🔢 Full evaluation

# Test 2: Mixed variables and constants
# Tree:    +        Result:    +
#         / \               / \
#        x   3             x   3
node2 = Node('+')
node2.left = Node('x')
node2.right = Node('3')
result2 = simplify_expression_tree(node2)
print(result2.value == '+' and result2.left.value == 'x' and result2.right.value == '3')  # 🔤 Variable preserved

# Test 3: Partial simplification
# Tree:      +          Result:    +
#          /   \                 /   \
#         *     -               6     5
#        / \   / \
#       2   3 8   3
node3 = Node('+')
node3.left = Node('*')
node3.right = Node('-')
node3.left.left = Node('2')
node3.left.right = Node('3')
node3.right.left = Node('8')
node3.right.right = Node('3')
result3 = simplify_expression_tree(node3)
print(result3.value == '+' and result3.left.value == '6' and result3.right.value == '5')  # 📊 Subtree simplification

# Test 4: All variables
# Tree:    +        Result:    + (unchanged)
#         / \               / \
#        x   y             x   y
node4 = Node('+')
node4.left = Node('x')
node4.right = Node('y')
result4 = simplify_expression_tree(node4)
print(result4.value == '+' and result4.left.value == 'x' and result4.right.value == 'y')  # 🔤 No simplification

# Test 5: Complex nested simplification
# Tree:          +               Result:    +
#              /   \                      /   \
#             /     \                    5     *
#            / \     \                        / \
#           2   3     *                      z   4
#                    / \
#                   z   4
node5 = Node('+')
node5.left = Node('/')
node5.right = Node('*')
node5.left.left = Node('10')
node5.left.right = Node('2')
node5.right.left = Node('z')
node5.right.right = Node('4')
result5 = simplify_expression_tree(node5)
print(result5.value == '+' and result5.left.value == '5' and 
      result5.right.value == '*' and result5.right.left.value == 'z')  # 🧮 Mixed simplification
