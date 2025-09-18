sum = 0

for i in range(1, int(input("Enter number: ")) + 1):
    if i % 3 == 0 or i % 5 == 0:
        sum += i
print("Sum of all numbers divisible by 3 or 5 is:", sum)
