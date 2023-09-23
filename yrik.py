WHITE = '\u001b[47m'
BLACK = '\u001b[40m'
END = '\u001b[0m'

for i in range (7):
    if i ==  0 or i == 6:
        print(f'{WHITE}{"  " * 3}{BLACK}{"  " * 1}{WHITE}{"  " * 5}{BLACK}{"  " * 1}{WHITE}{"  " * 3}{END}')
    if i ==  1 or i == 5:
        print(f'{WHITE}{"  " * 2}{BLACK}{"  " * 1}{WHITE}{"  " * 1}{BLACK}{"  " * 1}{WHITE}{"  " * 3}{BLACK}{"  " * 1}{WHITE}{"  " * 1}{BLACK}{"  " * 1}{WHITE}{"  " * 2}{END}')
    if i ==  2 or i == 4:
        print(f'{WHITE}{"  " * 1}{BLACK}{"  " * 1}{WHITE}{"  " * 3}{BLACK}{"  " * 1}{WHITE}{"  " * 1}{BLACK}{"  " * 1}{WHITE}{"  " * 3}{BLACK}{"  " * 1}{WHITE}{"  " * 1}{END}')
    if i ==  3:
        print(f'{BLACK}{"  " * 1}{WHITE}{"  " * 5}{BLACK}{"  " * 1}{WHITE}{"  " * 5}{BLACK}{"  " * 1}{END}')