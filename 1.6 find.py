import random

n = int(input("Введите длину массива: "))

arr = [random.randint(1, 10) for number in range(n)]
print(arr)
m = int(input("Какое число хотите найти: "))
print(arr.index(m))
