import math as m

line_str = input("длина стороны: ")

def square():

    line = float(line_str)

    line = m.ceil(line)

    print("Площадь квадрата: ", line*line)

square()