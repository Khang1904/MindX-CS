ls = map(int, input().split())


def getUniqueElements(ls):
    seen = set()
    seenTwice = set()
    for item in ls:
        if item not in seen and item not in seenTwice:
            seen.add(item)
        else:
            seen.discard(item)
            seenTwice.add(item)
    return list(seen)


print(getUniqueElements(ls))
