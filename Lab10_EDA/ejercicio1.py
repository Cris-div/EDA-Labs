def infix_to_postfix(tokens):
    """Convert infix expression to postfix notation"""
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2}  # 📊 Operator precedence
    stack = []  # 📚 Operator stack
    postfix = []  # 📝 Result

    for token in tokens:
        if token not in precedence and token not in '()':
            postfix.append(token) # 🔢 Add operand
        elif token =='(':
            stack.append(token) # 📥 Push (
        elif token==')':
            while stack and stack[-1]!='(':
                postfix.append(stack.pop()) # 📤 Pop operators
            stack.pop()  # Remove (
        else:
            while(stack and stack[-1]!='(' and 
                  stack[-1] in precedence and 
                  precedence[stack[-1]] >= precedence[token]): #:v evaluate the hierarchy of operators 
                postfix.append(stack.pop()) # 📤 Pop higher precedence
            stack.append(token) # 📥 Push operator

    while stack:
        postfix.append(stack.pop())  # 📤 Pop remaining
    
    return postfix

                

# ✅ Test cases
# Test 1: Simple addition
# Input: 2 + 3
# Output: 2 3 +
print(infix_to_postfix(['2', '+', '3']) == ['2', '3', '+'])  # ➕ Simple operation

# Test 2: Operator precedence
# Input: 2 + 3 * 4
# Output: 2 3 4 * +
print(infix_to_postfix(['2', '+', '3', '*', '4']) == ['2', '3', '4', '*', '+'])  # 📊 Precedence test

# Test 3: Parentheses override precedence
# Input: (2 + 3) * 4
# Output: 2 3 + 4 *
print(infix_to_postfix(['(', '2', '+', '3', ')', '*', '4']) == ['2', '3', '+', '4', '*'])  # 🔗 Parentheses

# Test 4: Complex expression
# Input: (1 + 2) * (3 - 4)
# Output: 1 2 + 3 4 - *
print(infix_to_postfix(['(', '1', '+', '2', ')', '*', '(', '3', '-', '4', ')']) == ['1', '2', '+', '3', '4', '-', '*'])  # 🧮 Complex

# Test 5: Multiple operators
# Input: a + b * c / d
# Output: a b c * d / +
print(infix_to_postfix(['a', '+', 'b', '*', 'c', '/', 'd']) == ['a', 'b', 'c', '*', 'd', '/', '+'])  # 🔤 Variables
