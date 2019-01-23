import random

answer = random.randint(0,101)

while True:
    num = input ("Введите число: ")
    if not num or num == "exit":
        break
    elif not num.isdigit():
        print ("Введите целое число!")
        continue

    user_guess = int(num)

    if user_guess > answer:
        print("Загаданное число меньше")
    elif user_guess < answer:
        print("Загаданное число больше")
    else:
        print ("Совершенно верно!")
        break