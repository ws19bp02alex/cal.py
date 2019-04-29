""" enter your weight and length of time you train a day. your weight"""
""" and time will give us your total calories burned"""

time = int(input('HOW MANY MINTUES TO YOU TRAIN A DAY?'))
weight =int(input('HOW MUCH DO YOU WEIGHT?'))
calories = time * 13.2
    if weight <=150:
        print(calories)
    else:
        calories = time * 17.9
        print(calories)

        

