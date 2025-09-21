def hot_potato(q, k):
    idx = 0
    while len(q) > 1:
        idx = (idx + k - 1) % len(q)
    return q[0] if len(q) == 1 else None


print(hot_potato(input("Enter players: ").split(), int(input("Enter a number: "))))
