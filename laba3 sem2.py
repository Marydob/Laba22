#1
import random
n = random.randint(2, 8)
print("Введите", n, "слов/а")
string = " "
for i in range(n):
    word = input(f"Введите {i+1} слово: ")
    string+=word + " "
print(string.strip())
#2
string = " "
while True:
    word = input("Введите слово (для завершения введите 'stop'): ")
    if word == 'stop':
        break
    string += word + " "
print(string)

#3
x = input("введите слово: ")
if ('ф' in x):
    print("Ого! Это редкое слово!")
else:
    print("Эх, это не очень редкое слово...")

#4
import random
right=0
wrong=0
while wrong<3:
    a=random.randint(1,9)
    b=random.randint(1,9)
    c= input(f"{a} + {b} = ")
    if  int(c)==a+b:
        print("Правильно!")
        right += 1
    else:
        print("Ответ неверный")
        wrong+= 1
else:
    print("Игра окончена.")
print("у тебя",right,"правильных ответа/ов и " , wrong, "неправильных")




