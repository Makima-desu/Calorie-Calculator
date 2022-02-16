import getpass
import csv
from datetime import *

#Returns the date of today
def getDate():
    month = date.today().strftime("%B")
    day = date.today().strftime("%d")
    year = date.today().strftime("%Y")
    date_string = f"{month} {day} {year}:"
    return date_string

#Parse thorugh the csv to allow us to check for ingredients
def parseFoodcsv():
    
    print("Parsing food CSV...")

    with open('Foods.csv', mode='r') as data:
        reader = csv.reader(data)

        return { rows[0]: rows[1] for rows in reader }

#Input the ingredient names in a list 
def getFoodEaten():
    foods_eaten = []

    food = ""

    while True:
        food = input("Food eaten (q to finish): ")

        if food == 'q':
            break
        
        foods_eaten.append(food)

    return foods_eaten
    
#A function to take user input for calculating calories
def eatenFood(food):
    total_calories = 0

    food_list = getFoodEaten() 

    for food_name, calories in food.items():
        if food_name in food_list:
            total_calories += int(calories)

    return str(total_calories) + ' ' + 'Calories eaten'

# Outputs into a file named Calorie.txt
def writeToFile(date, calorie_form, food_eaten):
    user_name = getpass.getuser()
    with open("C:/Users/" + user_name + "/Desktop/Calorie Tracker.txt", "a") as file:
        text_list = []

        text_list.append( (date, calorie_form, food_eaten) )

        for value in text_list:
            (date, calorie_form, food_eaten) = value
            line = "{}\n{}\n{}\n".format(date, calorie_form, food_eaten)
            file.write(line)
            file.write('\n')
            file.close()

    
# Uses a formula to calculate the calories you need daily to maintain weight
def calorieFormula(gender, exercise, male_calories, female_calories): 
    cal_per_day = 'Calories to maintain weight'

    if gender== 'M' and exercise == 'Sedentary':
        return str(male_calories * 1.20) + ' ' + cal_per_day
    elif gender== 'M' and exercise == 'Light':
        return str(male_calories * 1.37) + ' ' + cal_per_day
    elif gender== 'M' and exercise == 'Moderate':
        return str(male_calories * 1.46) + ' ' + cal_per_day
    elif exercise == "Active" and gender== 'M':
        return "{:.2f}".format(round(male_calories * 1.55, 2)) + ' ' + cal_per_day
    elif gender== 'M' and exercise == 'Very Active':
        return str(male_calories * 1.72) + ' ' + cal_per_day
    elif gender== 'M' and exercise == 'Extra Active':
        return str(male_calories * 1.90) + ' ' + cal_per_day
    elif gender== 'F' and exercise == 'Sedentary':
        return str(female_calories * 1.20) + ' ' + cal_per_day
    elif gender== 'F' and exercise == 'Light':
        return str(female_calories * 1.37) + ' ' + cal_per_day
    elif gender== 'F' and exercise == 'Moderate':
        return str(female_calories * 1.46) + ' ' + cal_per_day
    elif exercise == "Active" and gender== 'F':
        return "{:.2f}".format(round(female_calories * 1.46, 2)) + ' ' + cal_per_day
    elif gender== 'F' and exercise == 'Very Active':
        return str(female_calories * 1.72) + ' ' + cal_per_day
    elif gender== 'F' and exercise == 'Extra Active':
        return str(female_calories * 1.90) + ' ' + cal_per_day

#Main function which activates the program by calling other functions
def main():
    weight, height, age = input("Input your weight, height and age. It is a metric system.\n> ").split()
    male_calories = 10 * float(weight) + 6.25 * float(height) - 5 * float(age) + 5
    female_calories = 10 * float(weight) + 6.25 *float(height) - 5 * float(age) - 161
    gender = input('Gender\n> ')
    exercise = input('Exercise level\n> ')

    date = getDate()
    calorie_form = calorieFormula(gender, exercise, male_calories, female_calories)
    food = parseFoodcsv()
    food_eaten = eatenFood(food) 
    writeToFile(date, calorie_form, food_eaten)

if __name__ == "__main__":
    main() 
