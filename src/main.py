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

print('\nзадание 3: график функции y=2x+3\n')	

plot_list = [[0 for i in range(10)] for i in range(10)]
result = [0 for i in range(10)]

for i in range(10):
    result[i] = 2 * i + 3

start_y = 3
step_y = 2

for i in range(10):
    for j in range(10):
        if j == 0:
            plot_list[i][j] = start_y + step_y * (8 - i)

for i in range(9):
    for j in range(10):
        if abs(plot_list[i][0] - result[9 - j]) < step_y:
            for k in range(9):
                if 8 - k == j:
                    plot_list[i][k + 1] = 1

for i in range(9):
    line = ''
    for j in range(10):
        if j == 0:
            line += '\t' + str(int(plot_list[i][j])) + '\t'
        if plot_list[i][j] == 0:
            line += '--'
        if plot_list[i][j] == 1:
            line += '!'
    print(line)

print('\t0\t1 2 3 4 5 6 7 8 9')

print('\nзадание 4: диаграмма соотношения: сумма по модулю первых 125 чисел и вторых 125 чисел\n')

file = open('src/sequence.txt', 'r')
list = []
for number in file:
    list.append(float(number))
file.close()

if len(list) >= 250:
    sum_first_125 = sum(abs(x) for x in list[:125])
    sum_second_125 = sum(abs(x) for x in list[125:250])
    
    total_sum = sum_first_125 + sum_second_125
    
    percent_first = (sum_first_125 / total_sum) * 100
    percent_second = (sum_second_125 / total_sum) * 100

    length = 50
    
    first_bars = int(percent_first * length / 100)
    second_bars = int(percent_second * length / 100)
    
    print("Первые 125 чисел: ", end="")
    print("█" * first_bars + f" {percent_first:.1f}%")
    print("Вторые 125 чисел: ", end="")
    print("█" * second_bars + f" {percent_second:.1f}%")

# print('допольнительное задание: анимация')

# import os
# import time

# def clear_console():
#     os.system('cls' if os.name == 'nt' else 'clear')

# def heart():    
#     frames = [
#         [
#             "              ",
#             "              ",
#             "              ",
#             "      █ █     ",
#             "     █████    ",
#             "      ███     ",
#             "       █      ",
#             "              ",
#             "              "
#         ],
#         [
#             "              ",
#             "              ",
#             "    ██  ██    ",
#             "   ████████   ",
#             "    ██████    ",
#             "     ████     ",
#             "      ██      ",
#             "              ",
#             "              "
#         ],
#         [
#             " ███      ███ ",
#             "█████    █████",
#             "██████  ██████",
#             " ████████████ ",
#             "  ██████████  ",
#             "   ████████   ",
#             "    ██████    ",
#             "     ████     ",
#             "      ██      "
#         ]
#     ]
    
#     colors = [198, 196, 160]
#     frame_count = 0
#     while True:
#         clear_console()
        
#         color = colors[frame_count % len(colors)]
#         current_frame = frames[frame_count % len(frames)]
        
#         print(f"\nдополнительное задание: анимация \n")
        
#         for line in current_frame:
#             colored_line = ""
#             for char in line:
#                 if char == '█':
#                     colored_line += f'\x1b[38;5;{color}m{char}\x1b[0m'
#                 else:
#                     colored_line += char
#             print(f"{' ' * 20}{colored_line}")
        
#         frame_count += 1
#         time.sleep(0.5)

# if __name__ == "__main__":
#     try:
#         heart()
#     except KeyboardInterrupt:
#         clear_console()