"""
Написать программу, которая из имеющегося массива строк формирует новый 
массив из строк, длина которых меньше, либо равна 3 символам. 
Первоначальный массив можно ввести с клавиатуры, либо задать на старте 
выполнения алгоритма. При решении не рекомендуется пользоваться 
коллекциями, лучше обойтись исключительно массивами.

Примеры:
[“Hello”, “2”, “world”, “:-)”] → [“2”, “:-)”]
[“1234”, “1567”, “-2”, “computer science”] → [“-2”]
[“Russia”, “Denmark”, “Kazan”] → []
"""

# array = input("Write your words: ").split()

def filter_strings(array):
    result_array = []
    for string in array:
        if len(string) <= 3:
            result_array.append(string)
    return result_array        
    
print(filter_strings(array))
