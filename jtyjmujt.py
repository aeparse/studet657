for i in range (15):
    if i%3 != 0:
        if 2 < i < 13:
            print(12-i, ' |')
        elif i < 13:
             print(12 - i, '|')
        elif i == 13:
            print('    _____________________')
            print('      0 1 2 3 4 5 6 7 8 9')
    else:
        if 2 < i < 13:
            print(12-i, ' |', '  '*((12-i)//3), '*')
        elif i < 13:
             print(12 - i, '|', '  '*((12-i)//3), '*')

print(i, '1')




