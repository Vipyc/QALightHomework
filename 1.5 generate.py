import random


def generate(array,a,b):
    print("После генерации", [random.randint(a, b) for element in array])


arr = list(range(10))

a = int(input("Маленькое: "))
b = int(input("Большое: "))

print("Сначала", arr)
generate(arr, a, b)