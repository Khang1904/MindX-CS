menu = {"bánh": 5000, "kẹo": 2000, "sữa": 10000}
order = input("Nhập món bạn muốn gọi: ")
quantity = int(input("Nhập số lượng: "))

print(
    f"Tổng giá: {menu[order] * quantity} VND"
    if order in menu
    else "Món bạn gọi không có trong thực đơn"
)
