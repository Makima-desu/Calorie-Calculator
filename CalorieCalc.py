import getpass
import csv
from datetime import *


#Returns the date of today so that it can be referenced later when output into the file
def getDate():

    month = date.today().strftime("%B")
    day = date.today().strftime("%d")
    year = date.today().strftime("%Y")
    date_string = f"{month} {day} {year}:"
    return date_string

#A function to parse through food table csv
def foodTablecsv():

    #This opens the file specifically to parse only the names of the foods for you to choose from
    with open('Foods.csv', mode='r') as foods:
        file = csv.reader(foods)
        for read in file:
            print(read[0])

    print("Choose names from the list above:")
      
    #Opens the food table to access the names that we input. such as "potato"
    with open('Foods.csv', mode='r') as data:
        reader = csv.reader(data)
        row = { rows[0].lower(): rows[1].lower() for rows in reader }

        return row

    
#Function to get the user to input food names 
def getFoodEaten():

    foods_eaten = []

    food = ""

    while True:
        food = input("Food eaten (q to finish): ").lower()
        if food == 'q':
            break
        
        foods_eaten.append(food)

    return foods_eaten
    
#Function that takes getFoodEaten() function and calculates the total sum of the ingredients found
def eatenFood(foodDict):

    total_calories = 0
    food_list = getFoodEaten()

    for food_name in food_list:
        if food_name in foodDict.keys():
            print('Found {}'.format(food_name))
            
            total_calories += int(foodDict[food_name])

    return str(total_calories) + ' ' + 'Calories eaten'

# Outputs into a file named Calorie.txt. 
# date, takes in the getDate() function and return the date of today.
# calorie_form takes in the calorieFormula() function and outputs it into the file
# food_eaten takes in eatenFood() function and outputs it into the file
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
# gender is used in the formula such as Female or Male
# exercise is the level of exercise used in the formula
# male calories is the specific formula used for males
# female_calories is the specific formula used for females
def calorieFormula(gender, exercise, male_calories, female_calories): 

    cal_per_day = 'Calories to maintain weight'

    if gender == 'M' and exercise == 'sedentary':
        return str(male_calories * 1.20) + ' ' + cal_per_day
    elif gender == 'M' and exercise == 'light':
        return str(male_calories * 1.37) + ' ' + cal_per_day
    elif gender == 'M' and exercise == 'moderate':
        return str(male_calories * 1.46) + ' ' + cal_per_day
    elif exercise == "active" and gender== 'M':
        return "{:.2f}".format(round(male_calories * 1.55, 2)) + ' ' + cal_per_day
    elif gender == 'M' and exercise == 'very active':
        return str(male_calories * 1.72) + ' ' + cal_per_day
    elif gender == 'M' and exercise == 'extra active':
        return str(male_calories * 1.90) + ' ' + cal_per_day
    elif gender == 'F' and exercise == 'sedentary':
        return str(female_calories * 1.20) + ' ' + cal_per_day
    elif gender == 'F' and exercise == 'light':
        return str(female_calories * 1.37) + ' ' + cal_per_day
    elif gender == 'F' and exercise == 'moderate':
        return str(female_calories * 1.46) + ' ' + cal_per_day
    elif exercise == "active" and gender== 'F':
        return "{:.2f}".format(round(female_calories * 1.46, 2)) + ' ' + cal_per_day
    elif gender == 'F' and exercise == 'very active':
        return str(female_calories * 1.72) + ' ' + cal_per_day
    elif gender == 'F' and exercise == 'extra active':
        return str(female_calories * 1.90) + ' ' + cal_per_day

#Main function which activates the program by calling other functions
def main():

    exercises = ['Sedentary: Little or no exercise', 'Light: Exercise 1-3 times/week', 'Moderate: Exercise 4-5 times/week', 'Active: Daily exercise or intense exercise 3-4 times/week', 'Very Active: Intense exercise 6-7 times/week', 'Extra Active: Very intense exercise daily, or physical job' ]
    
    print('Example: 63 174 17. Weight, Height, Age')
    weight, height, age = input("Input your weight, height and age. It is a metric system.\n> ").split()

    male_calories = 10 * float(weight) + 6.25 * float(height) - 5 * float(age) + 5
    female_calories = 10 * float(weight) + 6.25 *float(height) - 5 * float(age) - 161

    gender = input('Gender: M for Male / F for Female\n> ').upper()
    
    for exercise in exercises:
        print(exercise)
    print('Choose your exercise level from the list above:')   
    exercise = input('> ').lower()
    print('---------------------------------------')

    date = getDate()
    calorie_form = calorieFormula(gender, exercise, male_calories, female_calories)
    foodDict = foodTablecsv
    food_eaten = eatenFood(foodDict) 
    writeToFile(date, calorie_form, food_eaten)

if __name__ == "__main__":
    main() 
