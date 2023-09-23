RED = '\u001b[41m'
WHITE = '\u001b[47m'
END = '\u001b[0m'

for i in range(10):
    if i == 0 or i ==8 or i == 1 or i ==9:
        print(f'{WHITE}{"   "*12}{END}')
    if i ==2 or i ==7:
        print(f'{WHITE}{"   " * 4}{RED}{"   " * 4}{WHITE}{"   " * 4}{END}')
    if i ==3 or i ==6:
        print(f'{WHITE}{"  " * 5}{RED}{"  " * 8}{WHITE}{"  " * 5}{END}')
    if i == 4 or i == 5:
        print(f'{WHITE}{"   " * 3}{RED}{"   " * 6}{WHITE}{"   " * 3}{END}')

