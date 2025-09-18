def binarySearchMatrix(matrix, target):
    matrix1D = []
    for row in matrix:
        matrix1D.extend(row)

    n = len(matrix1D)
    for i in range(n):
        for j in range(0, n - i - 1):
            if matrix1D[j] > matrix1D[j + 1]:
                matrix1D[j], matrix1D[j + 1] = matrix1D[j + 1], matrix1D[j]

    left, right = 0, len(matrix1D) - 1
    while left <= right:
        mid = (left + right) // 2
        if matrix1D[mid] == target:
            return True
        elif matrix1D[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return False


matrix = []
rows = int(input("Enter height of matrix: "))
for i in range(rows):
    matrix.append(
        list(map(int, input(f"Enter row {i + 1} (space-separated integers): ").split()))
    )

target = int(input("Enter target number: "))

print("Number found." if binarySearchMatrix(matrix, target) else "Number not found.")
