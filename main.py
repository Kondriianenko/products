import random
n = random.randint(1,20)
print("Гра розпочалась! Вгадай число 1-20!")
a=int(input("Введіть будь ласка число."))
while a!=n:
    print("Ви невгадали.")
    if n>a:
        print("число більше")
    elif n<a:
        print("число меньше")
    else:
        print("u win!")
        break
    a = int(input("Введіть будь ласка число."))
