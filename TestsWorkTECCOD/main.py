''' Функция для получения уникальных элементов из списка '''
def unique_el(int_list) -> list:
    return list(set(int_list))

print(unique_el([4, 2, 1, 4]))  # [1, 2, 4]



''' Фунция для поиска простых чисел в диапазоне '''
def prime_int(y):
    if y < 2:
        return False
    for i in range(2, int(y **0.5) + 1):
        if y % i == 0:
            return False
    return True

def primes_range(min, max):
    prime = []
    for num in range(min, max + 1):
        if prime_int(num):
            prime.append(num)
    return prime


''' Создать класс Point для представление точки в двумерном пространстве '''
import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    
    def to(self, other_point):
        return math.sqrt((self.x - other_point.x) ** 2 + (self.y, other_point.y) ** 2)
    
    def cordinator(self):
        return self.y, self.x

    def set_cordinator(self, y, x):
        self.x = x
        self.y = y

''' Сортировк списка строк по длине '''
def sorted_length(string, descord=False):
    return sorted(string, key=len, reverse=descord)


