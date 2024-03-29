# *ОПИСАНИЕ*

## *Фильтрация строк по длине в Python*

Программа, написанная на языке программирования Python, предназначена 
для фильтрации массива строк по их длине. Отфильтрованные строки включают 
те, длина которых меньше или равна 3 символам.

## *Как использовать*

**1.** Запустите программу, используя интерпретатор Python.

**2.** Введите строки через пробел, когда программа запросит ввод.

**3.** Программа выведет исходный массив строк и массив строк с длиной меньше или равной 
трём символам (если таких данных нет, программа выведет сообщение).

## *Как это работает*

>*user_input = input("Enter your data with space: ").split()*

Запрашивает у пользователя ввод данных, разделенных пробелами, и использует метод *split()* для разделения введенной строки на отдельные элементы списка. Результат сохраняется в переменной *user_input*.

>*def filter_strings(array)* 

Определяет функцию *filter_strings*, которая принимает массив строк в качестве аргумента.

>*result_array = []* 
    
Инициализирует пустой массив *result_array*, который будет содержать строки, 
удовлетворяющие условию.

>*for string in array*

Запускает цикл по каждой строке во входном массиве.

>*if len(string) <= 3* 

Проверяет, что длина текущей строки не превышает 3 символа.

>*result_array.append(string)* 

Если условие выполняется, добавляет текущую строку в итоговый массив *result_array*.

>*return result_array if any(result_array) else "no eligible data"* 

Возвращает значение итогового массива *result_array*, если он содержит хотя бы одну строку, удовлетворяющую условию. Если массив пуст (вследствии того, что данные не были введены пользователем, или отсутствуют данные, соответствующие условию), возвращает строковое сообщение *"no eligible data"*.

>*print(f'{user_input} -> {filter_strings(user_input)}')* 

Выводит исходный массив данных *user_input* и результат работы функции *filter_strings*.

Таким образом, программа фильтрует строки введенного массива, оставляя только те, длина которых не превышает 3 символа, и выводит результат, включая исходные данные и отфильтрованный массив.

