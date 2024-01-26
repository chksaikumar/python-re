print("The Area and Perimeter program")
print()
while True:
    length = int(input("Please enter the length: "))
    if length > 0:
        break
    else:
        print("Length must be greater than 0. Please try again.")
while True:
    width = int(input("Please enter the width: "))
    if width > 0:
        break
    else:
        print("Width must be greater than 0. Please try again.")
print()
area = length * width
perimeter = 2 * (length + width)
print("Area = " + str(area))
print("Perimeter = " + str(perimeter))
print()
print("Bye!")
