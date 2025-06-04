import sys
from array import array

# Определяем объём памяти, который занимает список из семнадцати чисел.
# Получим результат в байтах.
data_1 = [1] * 100
print(sys.getsizeof(data_1))

# Определяем объём памяти, который занимает array.
data_2 = array('b', data_1)
print(sys.getsizeof(data_2))
