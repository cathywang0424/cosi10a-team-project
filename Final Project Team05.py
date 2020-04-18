""" Final Group Project"""
# This is a calorie calculator.
import math

def calorie_calculator():
    print("*** Welcome! This is a calorie calculator. It will generate your ideal daily calorie intake and a one-day diet for you! ***")
    want_to_use = True

    while (want_to_use):
        print("We will gather some of your personal information to do the calculation.")
        age = int(input ("What is your age?"))
        sex = input ("What is your gender? Please enter m, f, or nonbinary.")
        height = float(input ("Please indicate your height in cm. e.g., if your height is 165cm, please enter 165."))
        weight = float(input ("Please indicate your weight in kg. e.g., if your weight is 55kg, please enter 55."))
        print("**********")
        print("Then we will ask you to indicate your activity level. If you do not exercise frequently, please enter 1.1. If you exercise somewhat frequently, please enter 1.2. If you exercise very frequently, please enter 1.3.")
        activity = float(input ("Please indicate your activity level."))

        if sex == "m":
            calorie = (660 + 1.38 * weight + 5 * height - 6.8 * age) * activity
        elif sex == "f":
            calorie = (655 + 9.6 * weight + 1.9 * height - 4.7 * age) * activity
        else:
            calorie = (660 + 1.38 * weight + 5 * height - 6.8 * age) * activity

        print("Your calculated ideal calorie per day is: ", math.ceil(calorie - 100), "~", math.ceil(calorie +150), "calories/day!")
        break

# design a one day diet according to the calorie range (including breakfast, lunch, dinner)
    # we can design a total of 20 diets for example, each have a different calorie content. then, we can randomly choose one that is within the range of the calorie intake
    # for instance, if the ideal calorie intake is from 1500-2000, the function will randomly return diets within that range
# ask the user if he or she is vegan(?)
# if yes, return a vegan diet
# if no, return a normal diet
# ask the user if he or she wants a snack (if yes, return a snack)
# print out the diet in a pretty format
# ask if the user want another day's diet
# if yes, circle back
# if not, exit the program
