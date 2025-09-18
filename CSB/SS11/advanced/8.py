def is_valid_html_tags(s):
    stack = []
    i = 0
    while i < len(s):
        if s[i] == "<":
            j = s.find(">", i)
            if j == -1:
                return False
            tag = s[i + 1 : j]
            if tag and tag[0] != "/":
                stack.append(tag)
            else:
                if not stack or stack[-1] != tag[1:]:
                    return False
                stack.pop()
            i = j + 1
        else:
            i += 1
    return not stack


if __name__ == "__main__":
    expr = input("Nhập chuỗi HTML/XML: ")
    if is_valid_html_tags(expr):
        print("Hợp lệ")
    else:
        print("Sai")
