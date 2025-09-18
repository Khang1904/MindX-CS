def duplicate(ls):
    seen = set()
    for item in ls:
        if item in seen:
            return True
        seen.add(item)
    return False
