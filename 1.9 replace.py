import random

def replace(list,i):
    newElement = int(input("Введите новый элемент: "))
    list[i] = newElement
    print(list)


length = int(input("Введите длину массива: \n"))
arr = [random.randint(1, 100) for n in range(length)]
print(arr)
index = int(input("Введите индекс: "))

replace(arr, index)
