import csv
class Food:
    def __init__(self, name, fat, carb, protein, kcal):
        self.name=name
        self.fat = fat
        self.carb = carb
        self.protein = protein
        self.kcal = kcal
    
foodList = []
dishList = []





with open('food.csv', 'r') as f:
    reader = csv.reader(f)
    for name, fat,carb,protein,kcal in reader:
        foodList.append(Food(name,fat,carb,protein,kcal))
    
def findFood():
    x = input("Type your food: ")
    for fd in foodList:
        if fd.name == x:
            grams = int(input("How much grams?: "))
            dishList.append([fd.name, 
                             (int(fd.fat)/100*grams), 
                             (int(fd.carb)/100*grams),
                             (int(fd.protein)/100*grams),
                             (int(fd.kcal)/100*grams)])
            print(dishList)



def calculateDish():
    fats = int(sum(x[1] for x in dishList))
    carbs = int(sum(x[2] for x in dishList))
    proteins = int(sum(x[3] for x in dishList))
    kcals = int(sum(x[4] for x in dishList))
    sumKcal = {}
    sumKcal['fats'] = fats
    sumKcal['carbs'] = carbs
    sumKcal['proteins'] = proteins
    sumKcal['kcals'] = kcals
    for key, value in sumKcal.items():
        print(key, value)
    return sumKcal
