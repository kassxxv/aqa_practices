from abc import ABC, abstractmethod

# 1
def calculate_sum_of_elements_in_array(array: list) -> list:
    results = []
    for elm in array:
        sum_for_elm = 0
        for el in elm.split(','):
            sum_for_elm += int(el)
        results.append(sum_for_elm)
    return results


# 2
class Student:
    def __init__(self, name: str, surname: str, age: int, avr_score: float):
        self.name = name
        self.surname = surname
        self.age = age
        self.avr_score = avr_score

    def change_score(self, new_score: float):
        self.avr_score = new_score
        return self.avr_score


# 3
def longest_word_in_a_list(list_of_words: list):
    if not list_of_words:
        return "", 0
    best_result = ''
    for word in list_of_words:
        if len(word) > len(best_result):
            best_result = word
    return best_result, len(best_result)


# 4
class Figure(ABC):
    @abstractmethod
    def get_area(self):
        pass

    @abstractmethod
    def get_perimeter(self):
        pass

    @property
    @abstractmethod
    def name(self):
        pass

class Square(Figure):
    def __init__(self, side):
        self.__side = side

    def get_area(self):
        return self.__side * self.__side

    def get_perimeter(self):
        return 4 * self.__side

    @property
    def name(self):
        return "Квадрат"


class Circle(Figure):
    def __init__(self, radius):
        self.__radius = radius

    def get_area(self):
        return 3.14 * (self.__radius ** 2)

    def get_perimeter(self):
        return 2 * 3.14 * self.__radius

    @property
    def name(self):
        return "Коло"