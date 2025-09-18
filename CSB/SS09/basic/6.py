scores = {"An": 8, "Bình": 6, "Châu": 9}
name = input("Nhập tên học sinh: ")

print(
    f"Điểm của {name} là: {scores.get(name, 'Không tìm thấy học sinh')}"
    if name in scores
    else f"Không tìm thấy học sinh {name}"
)
