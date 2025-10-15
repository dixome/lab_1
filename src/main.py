print('задание 1: флаг Бангладеша\n')	

GREEN = "\033[42m"
RED = "\033[41m"
END = "\033[0m"

WIDTH = 60
HEIGHT = 20

center_x = WIDTH // 3
center_y = HEIGHT // 2

radius = 5

def is_in_circle(x, y):
    return (x - center_x) ** 2 + (y - center_y) ** 2 <= radius ** 2

for y in range(HEIGHT):
    for x in range(WIDTH):
        if is_in_circle(x, y):
            print(RED + " ", end="")
        else:
            print(GREEN + " ", end="")
    print(END)