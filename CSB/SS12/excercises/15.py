def interleave_queue(q):
    if len(q) % 2 != 0:
        raise ValueError("Queue must have an even number of elements")

    m = len(q) // 2
    r = []
    q1 = q[:m]
    q2 = q[m:]
    for i in range(m):
        r.append(q1[i])
        r.append(q2[i])
    return r


print(interleave_queue([int(x) for x in input().split()]))
