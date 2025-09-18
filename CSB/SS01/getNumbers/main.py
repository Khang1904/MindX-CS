sum = 0

while True:
    try:
        num = int(input("Enter a number: "))
        sum += num
    except:
        print("Not a number.")
        print("Sum:", sum)
        break
