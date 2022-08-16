# I will come back here soon

from person import Person
from food import *

print("Hey, lets start! Type your data here:\n")
person = Person(name = input("name: "),
                age = int(input("age: ")),
                height = int(input("height(cm): ")),
                weight = int(input("weight(kg): ")),
                gender = input("gender(m/f): "))

while True:
    print("\nGreat! What do you want to do now?\n")
    print("Type '1' to calculate your BMI!")
    print("Type '2' to type and save your food!")
    print("Type '3' to print your food!")
    print("Type '4' to calculate your macro!")
    impt = input("Number: ")
    if impt == '1':
        print(person.calculateBMI())
    elif impt == '2':
        findFood()
    elif impt == '3':
        for i in dishList:
            print(i[0])
    elif impt == '4':
        calculateDish()
