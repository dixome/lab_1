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

print('задание 2: повторяющийся узор')	

BLACK = '\u001b[40m'
WHITE = '\u001b[47m'
END = '\u001b[0m'

WIDTH = 11
HEIGHT = 7
repeats = 5

for y in range(HEIGHT):
    for r in range(repeats):
        for x in range(WIDTH):
            if (y in [0, 6] or
                (y == 1 and x > 9) or
                (y == 2 and (1 < x < 8 or x > 9)) or 
                (y == 3 and (1 < x < 4 or x > 9)) or
                (y == 4 and (1 < x < 4 or x > 5)) or
                (y == 5 and 1 < x < 4)):
                print(f"{BLACK} {END}", end="")
            else:
                print(f"{WHITE} {END}", end="")
    print()