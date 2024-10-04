def inverted_triangle(height)
    for i in range(height, 0 , -1):
        print("*" * i)


try:
    height = int(input("Enter the height of the triangle: "))
    if height < 1:
