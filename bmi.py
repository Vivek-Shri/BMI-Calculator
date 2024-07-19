weight = float(input("Enter your weight in KG:- "))
height = float(input("Enter your height in M:- "))
# BMI = weight / (height * height)
BMI = weight / (height * height)
print(BMI)

if (BMI<16):
    print("You are severely underweight"), BMI  

elif (BMI<18.5):
    print("You are underweight"), BMI

elif (BMI < 24):
    print("You are normal"), BMI

elif (BMI < 30):
    print("You are overweight"), BMI

else:
    print("You are obese"), BMI

