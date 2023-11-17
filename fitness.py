import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import *
import sqlite3
import os

def main(): # determines if new user or existing user
    file_path = 'user_info.txt'

    if os.path.exists(file_path): # existing user
        main_menu()
    else: # new user, put them through orientation
        new_account()

# calculates calorie maintenence based on information from user
def calculate_maintenance(gender, age, height, weight, activity_level):
    if gender == "M":
        bmr = float(10 * (weight * 0.453592) + (6.25 * (height * 2.54)) - (5 * age) + 5)
    if gender == "F":
        bmr = float(10 * (weight * 0.453592) + (6.25 * (height * 2.54)) - (5 * age) - 161)

    maintenance = bmr * activity_level
    return maintenance


# for new users only. determines calorie maintenence, goals, and others
def new_account(): 
    print("Welcome to FitLife!")
    print("------------------------------------")
    username = input("Enter username: ")

    name = input("Enter name: ")
    gender = input("Enter M or F: ")
    while gender != "M" and gender != "F":
        gender = input("Enter M or F: ")

    age = int(input("Enter age: "))
    height = int(input("Enter height in inches: "))
    weight = float(input("Enter weight (lbs): "))
    print("How would you describe your activity level?")
    print("1. Sedentary: little or not exercise, work a desk job")
    print("2. Lightly Active: light exercise 1-3 days/week")
    print("3. Moderately Active: moderate exercise 3-5 days/week")
    print("4. Very Active: heavy exercise 6-7 days/week")
    print("5. Extremely Active: strenuous training 2x/day")
    activity_choice = int(input("--> "))

    if not (1 <= activity_choice <= 5):
        activity_choice = input("Please enter valid answer: ")
    if activity_choice == 1:
        activity_level = 1.2
    elif activity_choice == 2:
        activity_level = 1.375
    elif activity_choice == 3:
        activity_level = 1.55
    elif activity_choice == 4:
        activity_level = 1.725
    elif activity_choice == 5:
        activity_level = 1.9
    else:
        print("Error")
    
    maintenance = round(calculate_maintenance(gender, age, height, weight, activity_level))

    goal_weight = float(input("Goal weight: "))
    calorie_goal = 0
    
    if goal_weight < weight:
        goal = "loss"
        print("Choose a goal:")
        print("2. Extreme Weight Loss (2 lbs/week)")
        print("1.5. Rapid Weight Loss (1.5 lbs/week")
        print("1. Moderate Weight Loss (1 lb/week) *RECCOMENDED*")
        print("0.5. Gradual Weight Loss (0.5 lbs/week")
        weight_loss_speed = float(input("--> "))
        calorie_goal = find_calorie_goal(goal, weight_loss_speed, maintenance)
    elif goal_weight > weight:
        goal = "gain"
        print("Choose a goal:")
        print("2. Gain 2 lbs/week")
        print("1.5. Gain 1.5 lbs/week")
        print("1. Gain 1 lb/week")
        print("0.5. Gain 0.5 lbs/week")
        weight_gain_speed = float(input("--> "))
        calorie_goal = find_calorie_goal(goal, weight_gain_speed, maintenance)

    # 10 total items
    add_to_file = [username, name, gender, age, height, weight, goal_weight, maintenance, goal, calorie_goal]
    with open("user_info.txt", "w") as user_info: # adds all items in above list to text file
        for item in add_to_file:
            user_info.write(str(item) + "\n")

def find_calorie_goal(goal, speed, maintenance): 
    if goal == "loss":
        calorie_goal = maintenance - (speed * 500)
    if goal == "gain":
        calorie_goal = maintenance + (speed * 500)
    return calorie_goal

def main_menu():
    return None

main()