print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
def calculate_bmi(height, weight):
     print("Height = " + str(height))
     print("Weight = " + str(weight))
     bmi = float(weight/(height*height))
     print("bmi = " + str(bmi))
     if bmi < 18.5:
         return -1
     elif 18.5 <= bmi <= 25.0:
         return 0
     else:
         return 1

def user_input():
    height = float(input("Enter your height in meters: "))
    weight = float(input("Enter your weight in kilograms: "))
    return height,weight


height, weight = user_input()
print(calculate_bmi(height,weight))












