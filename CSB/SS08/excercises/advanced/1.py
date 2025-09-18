def selectionSortMatrix(matrix):
    for row in matrix:
        n = len(row)
        for i in range(n):
            min_index = i
            for j in range(i + 1, n):
                if row[j] < row[min_index]:
                    min_index = j
            row[i], row[min_index] = row[min_index], row[i]
    return matrix


matrix = []
for _ in range(int(input("Enter the height of the matrix:"))):
    row = [int(x) for x in input("Enter the row elements separated by space: ").split()]
    matrix.append(row)

print("Sorted matrix:", selectionSortMatrix(matrix))
