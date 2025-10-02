def sliding_window_max(q, k):
    result = []
    n = len(q)
    for i in range(n - k + 1):
        window = q[i : i + k]
        result.append(max(window))
    return result


print(
    sliding_window_max(
        list(map(int, input("Enter list of numbers: ").split())),
        int(input("Enter size of window")),
    )
)
