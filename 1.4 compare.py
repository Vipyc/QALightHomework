def compare(x, y, z):
    if x > y:
        print(z)
    elif x < y:
        print("Ваш долг по кредиту $10 000")
    elif x == y:
        print("Ваш долг переведен на вашу бывшую")


x = int(input("Введите первое число\n"))
y = int(input("Введите второе число\n"))
z = input("Введите строку\n")

compare(x, y, z)