# task 01 == Виправте синтаксичні помилки
print("Hello", end=" ")
print("world!")


# task 02 == Виправте синтаксичні помилки
hello = "Hello"
world = "world"
if True:
    print(f"{hello} {world}!")


# task 03  == Вcтавте пропущену змінну у ф-цію print
for letter in "Hello world!":
    print(letter)


# task 04 == Зробіть так, щоб кількість бананів була
# завжди в чотири рази більша, ніж яблук
apples = 2
banana = apples * 4


# task 05 == виправте назви змінних
side = 1
side_2 = 2
side_3 = 3
side_4 = 4


# task 06 == Порахуйте периметр фігури з task 05
# та виведіть його для користувача
perimeter = side + side_2 + side_3 + side_4
print(f'Периметер: {perimeter}')


"""
    # Задачі 07 -10:
    # Переведіть задачі з книги "Математика, 2 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в другому класі
"""
# task 07
"""
У саду посадили 4 яблуні. Груш на 5 більше яблунь, а слив - на 2 менше.
Скільки всього дерев посадили в саду?
"""
apple = 4
peer = apple + 5
plum = apple - 2
print(f'Загалом в саду посадили {apple + peer + plum} дерев.')


# task 08
"""
До обіда температура повітря була на 5 градусів вище нуля.
Після обіду температура опустилася на 10 градусів.
Надвечір потепліло на 4 градуси. Яка температура надвечір?
"""
start_temperature = 0
temperature_before_lunch = start_temperature + 5
temperature_after_lunch = temperature_before_lunch - 10
temperature_at_evening = temperature_after_lunch + 4
print(f'Температура надвечір: {temperature_at_evening} градусів цельсія.')


# task 09
"""
Взагалі у театральному гуртку - 24 хлопчики, а дівчаток - вдвічі менше.
1 хлопчик захворів та 2 дівчинки не прийшли сьогодні.
Скількі сьогодні дітей у театральному гуртку?
"""
boys = 24
girls = boys // 2
boy_get_ill = 1
girls_do_not_come = 2
print(f'Сьогодні пришло {boys + girls - boy_get_ill - girls_do_not_come} дітей у театральному гуртку.')


# task 10
"""
Перша книжка коштує 8 грн., друга - на 2 грн. дороже,
а третя - як половина вартості першої та другої разом.
Скільки будуть коштувати усі книги, якщо купити по одному примірнику?
"""
first_book = 8
second_book = first_book + 2
third_book = (first_book+second_book)//2
print(f'Ціна за усі книги по одному примірнику: {first_book + second_book + third_book} гривень.')
