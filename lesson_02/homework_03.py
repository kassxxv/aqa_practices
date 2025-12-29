from math import ceil

alice_in_wonderland = ('"Would you tell me, please, which way I ought to go from here?"\n'
                       '"That depends a good deal on where you want to get to," said the Cat.\n'
                       '"I don\'t much care where ——" said Alice.\n'
                       '"Then it doesn\'t matter which way you go," said the Cat.\n'
                       '"—— so long as I get somewhere," Alice added as an explanation.\n'
                       '"Oh, you\'re sure to do that," said the Cat, "if you only walk long enough."')
# task 01 == Розділіть змінну alice_in_wonderland так, щоб вона займала декілька фізичних лінії
# task 02 == Знайдіть та відобразіть всі символи одинарної лапки (') у тексті
for char in alice_in_wonderland:
    if char == "'":
        print(char)

print(alice_in_wonderland) # task 03 == Виведіть змінну alice_in_wonderland на друк

"""
    # Задачі 04 -10:
    # Переведіть задачі з книги "Математика, 5 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в п'ятому класі
"""
# task 04
"""
Площа Чорного моря становить 436 402 км2, а площа Азовського
моря становить 37 800 км2. Яку площу займають Чорне та Азов-
ське моря разом?
"""
black_sea_square = 436402
sea_of_azov_square = 37800
total_area = black_sea_square + sea_of_azov_square
print(f'\nПлоща Азовскього і Чорного моря разом : {total_area} км2')


# task 05
"""
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""
total_products = 375291
first_and_second_warehouse = 250449
second_and_third_warehouse = 222950
first_warehouse = total_products - second_and_third_warehouse
third_warehouse = total_products - first_and_second_warehouse
second_warehouse = total_products - first_warehouse + (total_products - third_warehouse)
print(f'\nНа першому складі {first_warehouse} товарів.\nНа другому складі {second_warehouse} товарів.\nНа третьому складі {third_warehouse} товарів.')

# task 06
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""
months = 12 * 1.5
monthly_payment = 1179
computer_price = months * monthly_payment
print(f"\nВартість комп'ютера - {computer_price}грн\n")

# task 07
"""
Знайди остачу від діленя чисел:
a) 8019 : 8     d) 7248 : 6
b) 9907 : 9     e) 7128 : 5
c) 2789 : 5     f) 19224 : 9
"""
a, b, c, d, e, f = 8019%8, 9907%9, 2789%5, 7248%6, 7128%5, 19224%9
print(f'Остача від ділення чисел:\na) 8019:8 = {a}\nb) 9907:9 = {b}\nc) 2789:5 = {c}\nd) 7248:6 = {d}\ne) 7128:5 = {e}\nf) 19224:9 = {f}')


# task 08
"""
Іринка, готуючись до свого дня народження, склала список того,
що їй потрібно замовити. Обчисліть, скільки грошей знадобиться
для даного її замовлення.
Назва товару    Кількість   Ціна
Піца велика     4           274 грн
Піца середня    2           218 грн
Сік             4           35 грн
Торт            1           350 грн
Вода            3           21 грн
"""
big_pizza_price = 4 * 274 # в виді кількість * ціна
medium_pizza_price = 2 * 218
juice_price = 4 * 35
cake_price = 1 * 350
water_price = 3 * 21
print(f'\nЗагалом Іринці знадобиться {big_pizza_price+medium_pizza_price+juice_price+cake_price+water_price} гривень для її замовлення.')

# task 09
"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""
print(f'\nІгорю знадобиться {ceil(232//8)} сторінок, щоб вклеїти всі фото.')

# task 10
"""
Родина зібралася в автомобільну подорож із Харкова в Буда-
пешт. Відстань між цими містами становить 1600 км. Відомо,
що на кожні 100 км необхідно 9 літрів бензину. Місткість баку
становить 48 літрів.
1) Скільки літрів бензину знадобиться для такої подорожі?
2) Скільки щонайменше разів родині необхідно заїхати на зап-
равку під час цієї подорожі, кожного разу заправляючи пов-
ний бак?
"""
distance_between_cities = 1600
tank_capacity = 48
fuel_needed = (1600//100)*9
print(f'\nДля такої подорожі знадобиться {fuel_needed} літрів бензину. \n'
      f'Родині потрібно заїхати щонайменше {ceil((fuel_needed - tank_capacity) / tank_capacity)} разів на заправку, заправляючи повний бак.') # виїдемо з повним баком