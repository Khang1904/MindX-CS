def postfix(eq):
    precedence = {"+": 1, "-": 1, "*": 2, "/": 2, "^": 3}
    postfix = []
    op = []

    for c in eq:
        if c.isalnum():
            postfix.append(c)
        else:
            while op and precedence[op[-1]] >= precedence[c]:
                postfix.append(op.pop())
            op.append(c)

    while op:
        postfix.append(op.pop())

    return " ".join(postfix)


print(postfix(input("Enter Infix Equation: ").split()))
