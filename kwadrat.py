def generate_square(size):
    tekst = ""
    for i in range(size):
        for j in range(size):
            if i == 0 or i == size - 1 or j == 0 or j == size - 1:
                tekst += "* "
            else:
                tekst += "  "
        tekst += "\n"
    return tekst

size = 10

square = generate_square(size)

file_name = "square.txt"

with open(file_name, "w") as file:
    file.write(square)
    def generate_triangle(size):
        tekst = ""
        for i in range(1, size + 1):
                tekst += "*" * i + "\n"
        return tekst

size = 7

triangle = generate_triangle(size)

file_name = "triangle.txt"

with open(file_name, "w") as file:
    file.write(triangle)

def generate_isosceles_triangle(size):
    tekst = ""
    for i in range(size):
        stars = 2 * i + 1
        spaces = size - stars // 2
        tekst += " " * spaces + "*" * stars + "\n"
    return tekst

size = 4

isosceles_triangle = generate_isosceles_triangle(size)

file_name = "isosceles_triangle.txt"

with open(file_name, "w") as file:
    file.write(isosceles_triangle)