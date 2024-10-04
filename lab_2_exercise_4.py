def inverted_triangle(height)
    for i in range(height, 0 , -1):
        print("*" * i)


try:
    height = int(input("Enter the height of the triangle: "))
    if height < 1:
        print("Invalid! Height must be 1 or greater.")
    else:
        inverted_triangle(height)

except ValueError:
