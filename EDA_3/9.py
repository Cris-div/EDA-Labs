def infix_to_postfix(tokens):
    output = []
    stack = []
    prec = {"+":1, "-":1, "*":2, "/":2}
    for token in tokens:
        if token.isalnum():
            output.append(token)
        elif token == "(":
            stack.append(token)
        elif token == ")":
            while stack and stack[-1] != "(":
                output.append(stack.pop())
            stack.pop()
        else:
            while stack and stack[-1] in prec and prec[token] <= prec[stack[-1]]:
                output.append(stack.pop())
            stack.append(token)
    while stack:
        output.append(stack.pop())
    return output
    

# 🧪 Test cases
def test_infix_to_postfix():
    print("➕ Test 1:", infix_to_postfix(["2", "+", "3"]) == ["2", "3", "+"])
    print("📊 Test 2:", infix_to_postfix(["2", "+", "3", "*", "4"]) ==
          ["2", "3", "4", "*", "+"])
    print("🔗 Test 3:", infix_to_postfix(["(", "2", "+", "3", ")", "*", "4"]) ==
          ["2", "3", "+", "4", "*"])
    print("🧮 Test 4:", infix_to_postfix(["(", "1", "+", "2", ")", "*", "(",
                                         "3", "-", "4", ")"]) ==
          ["1", "2", "+", "3", "4", "-", "*"])
    print("🔤 Test 5:", infix_to_postfix(["a", "+", "b", "*", "c", "/", "d"]) ==
          ["a", "b", "c", "*", "d", "/", "+"])

# 🚀 Run tests
test_infix_to_postfix()