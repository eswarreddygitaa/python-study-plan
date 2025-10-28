import random
import string

#1  # Write a function list_of_hexa_colors which returns a list of random HEX colors.
def list_of_hexa_colors(n):
    hex_colors = []
    for _ in range(n):
        color = '#' + ''.join(random.choice('0123456789abcdef') for _ in range(6))
        hex_colors.append(color)
    return hex_colors
print(list_of_hexa_colors(3))


#2  # Write a function list_of_rgb_colors which returns a list of random RGB colors.
def rgb_color_gen():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return f"rgb({r},{g},{b})"
def list_of_rgb_colors(n):
    rgb_colors = []
    for _ in range(n):
        color = rgb_color_gen()
        rgb_colors.append(color)
    return rgb_colors
print(list_of_rgb_colors(3))


#3  # Write a function generate_colors which can generate any number of hexa or rgb colors.
def generate_colors(color_type, n):
    color_type = color_type.lower()
    if color_type == 'hexa':
        return list_of_hexa_colors(n)
    elif color_type == 'rgb':
        return list_of_rgb_colors(n)
    else:
        return "Invalid color type! Use 'hexa' or 'rgb'."
print("generate_colors('hexa', 3):", generate_colors('hexa', 3))
print("generate_colors('hexa', 1):", generate_colors('hexa', 1))
print("generate_colors('rgb', 3):", generate_colors('rgb', 3))
print("generate_colors('rgb', 1):", generate_colors('rgb', 1))