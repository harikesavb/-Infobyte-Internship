#formula for BMI calculator
def formula_bmi(weight, height):
    bmi = weight/(height ** 2)

#Category in BMI
def process_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 24.9:
        return "Normal weight"
    elif bmi < 29.9:
        return "Overweight"
    elif bmi < 34.9:
        return "Moderately obese"
    elif bmi < 39.9:
        return "Severely obese"
    elif bmi <= 40.0:
        return "Morbidly obese"
    else:
        return "Obese"


#user-input Method to get the value's of weight and height from user
def start():
    try:
        weight = float(input("Enter your weight in kilograms: "))
        height = float(input("Enter your height in meters: "))

        if weight <= 0 or height <= 0:
            print("Invalid input! Your value must be greater than zero.")
        else:
            bmi = formula_bmi(weight, height)
            category = process_bmi(bmi)

            print(f"Your BMI is: {bmi}")
            print("Category:", category)

    except ValueError:
        print("Invalid input! Your value must be numeric values.")

 #Main program       
if __name__ == "__main__":
    start()