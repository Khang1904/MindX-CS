def postfix(eq):
    precedence = {"+": 1, "-": 1, "*": 2, "/": 2, "^": 3}
    postfix = []
    op = []

    for c in eq:
        if c.isalnum():
            postfix.append(c)
        elif c == "(":
            op.append(c)
        elif c == ")":
            while op and op[-1] != "(":
                postfix.append(op.pop())
            if op and op[-1] == "(":
                op.pop()
        else:
            while (
                op
                and op[-1] != "("
                and precedence.get(op[-1], 0) >= precedence.get(c, 0)
            ):
                postfix.append(op.pop())
            op.append(c)

    while op:
        postfix.append(op.pop())

    return postfix


def postfixEval(eq):
    stack = []
    for c in eq:
        if c.isnumeric():
            stack.append(int(c))
        else:
            try:
                b, a = stack.pop(), stack.pop()
            except Exception:
                raise ValueError("Invalid postfix expression")
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
    if not stack:
        raise ValueError("No result on stack")
    return stack[-1]


def tokenize(expr):
    import re

    # Split by space or keep operators/parentheses as separate tokens
    return re.findall(r"\d+|[a-zA-Z]+|[()+\-*/^]", expr)


if __name__ == "__main__":
    expr = input("Enter Infix Equation: ")
    tokens = tokenize(expr)
    try:
        pf = postfix(tokens)
        result = postfixEval(pf)
        print(result)
    except Exception as e:
        print("Error:", e)
