# Автор Ігор Хруневич
# Цю міні-програму створено, щоб зацікавити дітей програмуванням
# Користуйтесь, вивчайте, досліджуйте, змінюйте - експериментуйте

import turtle
print("Розрахуйте S площу прямокутника")

print("Введіть розміри сторін прямокутника:")
a = float(input("a довжина ? = "))
b = float(input("b ширина ? = "))
print ("S=a*b")
print("Площа = %.2f" % (a * b))
print ("Поки Ви звіряєте свій розвя'зок із розв'язком даної програми, черепашка намалювала Вам ваш прямокутник. Знайдіть його у себе на моніторі.")
turtle.forward(a*37)
turtle.left(90)
turtle.forward(b*37)
turtle.left(90)
turtle.forward(a*37)
turtle.left(90)
turtle.forward(b*37)
    
    

  
