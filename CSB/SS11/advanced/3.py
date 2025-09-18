def postfixEval(eq):
    stack = []
    for c in eq:
        if c.isnumeric():
            stack.append(int(c))
        else:
            b, a = stack.pop(), stack.pop()

            match c:
                case "+":
                    stack.append(a + b)
                case "-":
                    stack.append(a - b)
                case "*":
                    stack.append(a * b)
                case "/":
                    stack.append(a / b)
                case "^":
                    stack.append(a**b)
    return stack[-1]


print(postfixEval(input("Enter Postfix equation: ").split()))
