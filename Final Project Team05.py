""" Final Group Project"""
# This is a calorie calculator.
import math
import random
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

diet_vegan=[{'breakfast':'2 vegan pancakes with 1/4 cup blackberries and 1 Tbsp. peanut butter',
            'lunch':'1 serving white bean and avocado toast',
            'dinner':'1 serving Falafel Salad with lemmon Tahini dressing',
            'snack':'3/4 cup edamame pods','total_calories':'1200'},# 1200 cal
            {'breakfast':'1 serving peanut butter and Chia berry Jam English Muffin',
            'lunch':'4 cups White Bean Salad with olive oil and lemon dressing',
            'dinner':'2 cups black bean Quinoa Buddha bowl with avocado sauce',
            'snack':'1 Tbsp. dark chocolate chips',
            'total_calories':'1300'},# 1300 calorie
            {'breakfast':'1 serving peanut butter banana toast',
            'lunch':'4 cups Green Salad with beets and lemon dressing',
            'dinner':'1/2 cups roasted cauliflower with Asparagus',
            'snack':'4 Tbsp. pumpkin seeds',
            'total_calories':'1400'},# 1400 calorie
            {'breakfast':'1 serving strawberry cream cheese begal with 1 cup unsweetened soymilk',
            'lunch':'2 cups Black Bean Salad with potato curry soup',
            'dinner':'1 serving stuffed sweet potato with Hummus dressing',
            'snack':'2 Tbsp. dark chocolate chips',
            'total_calories':'1500'},# 1500 calorie
            {'breakfast':'2 vegan pancakes with chocolate croissant ',
            'lunch':'2 serving veggie and Hummus sandwich',
            'dinner':'1 serving potato curry with Asparagus',
            'snack':'2 Tbsp. dark chocolate chips and 1 Tbsp. pumpkin seeds',
            'total_calories':'1600'},# 1600 calorie
            {'breakfast':'2 cups Hummus with Raspberries',
            'lunch':'1 serving vegan Bistro lunch box',
            'dinner':'1 serving mush potato and roasted cauliflower',
            'snack':'1 Tbsp. potato chips',
            'total_calories':'1700'},# 1700 cal
            {'breakfast':'1 3/4 cup Muesli with Raspberries',
            'lunch':'2 cups Black Bean Salad with olive oil and lemon dressing',
            'dinner':'1 serving Poached Salmon with Asparagus and 3/4 cup Quinoa',
            'snack':'1 Tbsp. dark chocolate chips',
            'total_calories':'1800'},# 1800 calorie
            {'breakfast':'1 serving chocolate peanut protein shake',
            'lunch':'2 serving Grapefruit with roasted cauliflower',
            'dinner':'1 serving avocado Quesadillas',
            'snack':'1 Tbsp. Granola',
            'total_calories':'1900'},# 1900 cal
            {'breakfast':'1 cup Banana Chia smoothie',
            'lunch':'1 serving Almond butter and celery',
            'dinner':'1 serving tomato Spaghetti',
            'snack':'1 Tbsp. square white bread and peanut butter',
            'total_calories':'2000'},# 2000 calorie
            {'breakfast':'1 cup Raspberries fruit milk smoothie',
            'lunch':'2 cups Black Bean Salad and banana sandwich',
            'dinner':'1 serving Basal pasta with olive oil',
            'snack':'1 Tbsp. red bell pepper and Hummus',
            'total_calories':'2100'},# 2100 calorie
            {'breakfast':'1 cup Cinnamon apple bites and oat with soymilk',
            'lunch':'2 cups avocado toast sandwich',
            'dinner':'1 serving Spaghetti with mushroomm and tomato sauce',
            'snack':'1 Tbsp. dark chocolate chips and hummus',
            'total_calories':'2200'}]# 2200 calorie


def calorie_calculator():
    print("*** Welcome! This is a calorie calculator. It will generate your ideal daily calorie intake and a one-day diet for you! ***")
    want_to_use = True

    while (want_to_use):
        print("We will gather some of your personal information to do the calculation. ")
        age = int(input ("What is your age? "))
        print("----------")
        sex = input ("What is your gender? Please enter m, f, or nonbinary: ")
        print("----------")
        height = float(input ("Please indicate your height in cm (e.g., if your height is 165cm, please enter 165.): "))
        print("----------")
        weight = float(input ("Please indicate your weight in kg (e.g., if your weight is 55kg, please enter 55.): "))
        print("----------")
        vegan = input("Are you a vegan? Please enter y or n: ")
        print("----------")
        print("Then we will ask you to indicate your activity level.")
        print("If you do not exercise frequently, please enter 1.1.")
        print("If you exercise somewhat frequently, please enter 1.2.")
        print("If you exercise very frequently, please enter 1.3.")
        print("----------")
        activity = float(input ("Please indicate your activity level: "))
        print("----------")
        snack = input("Do you want snask options in your diet? Please enter y or n: ")
        print("----------")

        if sex == "m":
            calorie = (660 + 1.38 * weight + 5 * height - 6.8 * age) * activity
        elif sex == "f":
            calorie = (655 + 9.6 * weight + 1.9 * height - 4.7 * age) * activity
        elif vegan == "y":
            calorie = (655 + 9.6 * weight + 1.9 * height - 4.7 * age) * activity
        else:
            calorie = (660 + 1.38 * weight + 5 * height - 6.8 * age) * activity
        break

    lb = math.ceil(calorie - 100)
    ub = math.ceil(calorie + 150)

    if vegan == 'n':
        final_diet = []
        for i in diet:
            if int(i['total_calories']) >= lb and int(i['total_calories']) <=ub:
                final_diet.append(i)
                prettydiet = random.choice(final_diet)
                print("Your calculated ideal calorie per day is: ", lb, "~", ub, "calories/day!")
                print()
                print("Here is the diet selected for you: ")
                print()
                print('~ Breakfast: ',prettydiet['breakfast'])
                print('~ Lunch: ',prettydiet['lunch'])
                print('~ Dinner: ',prettydiet['dinner'])
                if snack == "y":
                    print('~ Snack: ',prettydiet['snack'])
                print('Total Calories: ',prettydiet['total_calories'])
                break
#for vegan choice, using new diet with the same calculation methods.
    if vegan == "y":
        final_diet_vegan = []
        for g in diet_vegan:
            if int(g['total_calories']) >= lb and int(g['total_calories']) <= ub:
                final_diet_vegan.append(g)
                prettydiet_vegan = random.choice(final_diet_vegan)
                print("Your calculated ideal calorie per day is: ", lb, "~", ub, "calories/day!")
                print()
                print("Here is the diet selected for you: ")
                print()
                print('~ Breakfast: ',prettydiet_vegan['breakfast'])
                print('~ Lunch: ',prettydiet_vegan['lunch'])
                print('~ Dinner: ',prettydiet_vegan['dinner'])
                if snack == "y":
                    print('~ Snack: ',prettydiet_vegan['snack'])
                print('Total Calories: ',prettydiet_vegan['total_calories'])
                print()

calorie_calculator()
