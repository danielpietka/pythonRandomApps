class Person:
    # Attributes
    def __init__(self, name, age, height, weight, gender):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
        self.gender = gender

    #persons = []

    def calculateBMI(self):
        
        inMeter = self.height / 100
        bmi = self.weight / inMeter**2
        if bmi < 18:
            print(f'Your BMI is {round(bmi, 2)}, you are underweight')
        elif bmi >= 18 and bmi < 25:
            print(f'Your BMI is {round(bmi, 2)}, you have normal weight')
        elif bmi >=25 and bmi < 30:
            print(f'Your BMI is {round(bmi, 2)}, you are overweight')
        else:
            print(f"Your BMI is {round(bmi, 2)}, go to gym bro")