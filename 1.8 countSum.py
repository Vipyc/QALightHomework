def count(arr):
    result = 0
    for num in arr:
        result += num

    print("Сумма элементов: ", result)


chislo = input("Введите число: ")
numberArray = [int(cifra) for cifra in list(chislo)]


count(numberArray)
