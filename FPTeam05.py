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


""" Diet options: """
diet=[{'breakfast':'1 3/4 cup Muesli with Raspberries',
        'lunch':'2 cups Black Bean Salad with olive oil and lemon dressing',
        'dinner':'1 serving Poached Salmon with Asparagus and 3/4 cup Quinoa',
        'snack':'1 Tbsp. dark chocolate chips',
        'total_calories':'1051'},  #1200 calories
        {'breakfast':'Blueberry-Banana Overnight Oats',
        'lunch':'2 cups Ravioli & Vegetable Soup with 2 slices baguette',
        'dinner':' Salmon & Vegetables',
        'snack':'4 Tbsp. hummus and 1 cup sliced cucumber',
        'total_calories':'1288'}, #1300 calories
        {'breakfast':'All Greens Smoothie Bowl',
        'lunch':'2 cups Ravioli & Vegetable Soup with 2 slices baguette',
        'dinner':'1 1/2 cups Squash & Tofu Curry with 1/2 cup brown rice',
        'snack':'1 medium apple and 3 Tbsp. unsalted dry-roasted almonds',
        'total_calories':'1321'}, #1400 calories
        {'breakfast':'Avocado & Arugula Omelet',
        'lunch':'Roasted Veggie Salad with chicken slices',
        'dinner':'Zucchini Noodles with Avocado Pesto & Shrimp',
        'snack':'1 Tbsp. dark chocolate chips, to enjoy after dinner',
        'total_calories':'1424'}, #1500 calories
        {'breakfast':'Scrambled Eggs with Vegetables and 1 banana',
        'lunch':'Apple & Cheddar Pita Pocket',
        'dinner':'1 Moroccan-Style Stuffed Pepper with 2 cups spinach',
        'snack':'1 medium apple with 2 Tbsp. peanut butter',
        'total_calories':'1506'}, #1600 calories
        {'breakfast':'Peanut Butter-Banana English Muffin and 1 medium orange',
        'lunch':'Chicken Tikka Masala',
        'dinner':'Taco Spaghetti with Squash',
        'snack':'1 medium apple and 1 Tbsp. nut butter',
        'total_calories':'1628'}, #1700 calories
        {'breakfast':'1 cup Greek yogurt with 1 cup Maple-Nut Granola and blueberries',
        'lunch':'Mediterranean Lettuce Wraps',
        'dinner':' Miso-Chicken Ramen',
        'snack':'1 medium apple and 1 Tbsp. nut butter',
        'total_calories':'1746'}, #1800 calories
        {'breakfast':'Strawberry-Ricotta Waffle Sandwich and a medium apple',
        'lunch':'1 1/2 Apple & Cheddar Pita Pocket',
        'dinner':'Goat Cheese Alfredo Pasta and Strawberry Cheesecake Shake',
        'snack':'4 Tbsp. hummus and 1 cup sliced cucumber',
        'total_calories':'1910'}, #1900 calories
        {'breakfast':'nut butter and banana toast and power smoothie',
        'lunch':'Taco Spaghetti Squash Boats',
        'dinner':'black bean and sweet potato burrito',
        'snack':'a small bag of chips',
        'total_calories':'2005'}, #2000 calories
        {'breakfast':'avocado toast with egg and greek yogurt with strawberries',
        'lunch':'philly cheesesteak sandwich with garlic mayo',
        'dinner':'2 slices of pepperoni pizza',
        'snack':'banana and almond butter',
        'total_calories':'2090'}, #2100 calories
        {'breakfast':'full English breakfast with a cup of coffee',
        'lunch':'Hot dog chili with feta chicken salad',
        'dinner':'Thai green curry with rice',
        'snack':'dried apricots with walnut halves',
        'total_calories':'2146'}] #2200 calories