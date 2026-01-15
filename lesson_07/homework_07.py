# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""
def multiplication_table(number):
    # Initialize the appropriate variable
    multiplier = 1

    # Complete the while loop condition.
    while True:
        result = number * multiplier
        # десь тут помила, а може не одна
        if  result > 25:
            # Enter the action to take if the result is greater than 25
            break
        print(f'{number}x{multiplier}={result}')
        # Increment the appropriate variable
        multiplier += 1

multiplication_table(3)
# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15


# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""
def sum_of_two(a, b):
    return a + b

print(f'Сума двох чисел: {sum_of_two(1, 4)}')


# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""
def arithmetic_mean(list_of_numbers : list) -> float:
    if not list_of_numbers:
        return 0.0
    return sum(list_of_numbers) / len(list_of_numbers)

print(f'Середнє арифметичне: {arithmetic_mean([1,2,3])}')


# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""
def reverse(string: str) -> str:
    return string[::-1]

print(f'Зворотний рядок: {reverse("Filip")}')


# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""
def longest_word_in_a_list(list_of_words: list):
    best_result = ''
    for word in list_of_words:
        if len(word) > len(best_result):
            best_result = word
    return best_result, len(best_result)

sample = ['Filip', 'Antonio', 'Hillel', 'QA', 'Automation_QA', 'NoMoney']
print(f'Найдовше слово зі списку та його довжина: {longest_word_in_a_list(sample)}')


# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""
def find_substring(string1:str, string2:str) -> int:
    return string1.find(string2)

str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2)) # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2)) # поверне -1

"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""


# task 7
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
def calculate_order_price(count_big_pizza:int, count_medium_pizza:int, juice_c:int, cake_c:int, water_c:int) -> str:
    total = (count_big_pizza * 274) + \
            (count_medium_pizza * 218) + \
            (juice_c * 35) + \
            (cake_c * 350) + \
            (water_c * 21)
    return f'\nЗагалом Іринці знадобиться {total} гривень для її замовлення.'

print(calculate_order_price(4, 2, 4, 1, 3))

# task 8
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
from math import ceil
def calculate_trip_details(distance:int, tank_capacity:int, per_100:int = 9) -> str:
    fuel_needed = (distance/100)*per_100
    refuels_needed = ceil(fuel_needed / tank_capacity) - 1
    return (f'Для такої подорожі знадобиться {fuel_needed} літрів бензину. \n'
      f'Родині потрібно заїхати щонайменше {refuels_needed} разів на заправку, заправляючи повний бак.')

print(calculate_trip_details(1600, 48))
# task 9
"""
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""
def warehouse_count(total:int, w1_w2:int, w2_w3:int):
    w1 = total - w2_w3
    w3 = total - w1_w2
    w2 = w1_w2 - w1
    return w1, w2, w3

wh1, wh2, wh3 = warehouse_count(375291, 250449, 222950)
print(f'Склад 1: {wh1}\nСклад 2: {wh2}\nСклад 3: {wh3}')


# task 10
"""
До обіда температура повітря була на 5 градусів вище нуля.
Після обіду температура опустилася на 10 градусів.
Надвечір потепліло на 4 градуси. Яка температура надвечір?
"""
def calculate_evening_temperature(start_temp: int) -> int:
    before_lunch = start_temp + 5
    after_lunch = before_lunch - 10
    evening = after_lunch + 4
    return evening

final_temp = calculate_evening_temperature(0)
print(f'Температура надвечір: {final_temp} градусів Цельсія.')