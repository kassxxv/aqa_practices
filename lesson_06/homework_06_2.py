n = 1
while True:
    inp = input(f'Спроба №{n} - Введіть слово яке містить літеру \'h\' або \'H\': ')
    n = n+1
    if 'h' in inp.lower():
        break