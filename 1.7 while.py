def compare(a, b, c):
    while not a >= b:
        print(a, " меньше чем ", b)
        a += c
    print("Цикл закончен, сдавайтесь")


one = int(input("Введите А: "))
two = int(input("Введите Б: "))
three = int(input("Введите В: "))

compare(one, two, three)
