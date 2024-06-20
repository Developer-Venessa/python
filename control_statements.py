age=int(input("enter age :"))
if age>=18:
    print("you are eligible to vote")
else:
    print("you are under age")

num=int(input("enter num :"))
if num%2==0:
    print(" it's an even number")
else:
    print("it's an odd number")


    marks=int(input("enter marks:"))
    if marks>=80 and marks<=100:
        print("you have an A")
    elif marks>=60 and marks<=79:
        print("you have a B")
    elif marks>=0 and marks<=59:
        print("you have failed")
    else:
        print("wrong input")

num1=int(input("enter the first number:"))
num2=int(input("enter the second number"))
num3=int(input("enter the third number"))
num4=int(input("enter the fourth number"))
if num1>num2 and num1>num3 and num1>num4:
    print(f"the largest number is {num1}")
elif num2>num1 and num2>num3 and num2>num4:
    print(f"the largest number is {num2}")
elif num3>num1 and num3>num2 and num3>num4:
    print(f"the largest number is {num3}")
elif num4>num1 and num4>num2 and num4>num3:
    print(f"the largest number is {num4}")
else:
    print("they are equal")

    # another example
if num1>num2 and num1>num3 and num1>num4:
    print(f"{num1} is greater than {num2,num3,num4}")
elif num1>num2 and num1>num3 and num1>num4:
    print(f"{num2} is greater than {num1,num3,num4}")
elif num1>num2 and num1>num3 and num1>num4:
    print(f"{num3} is greater than {num1,num2,num4}")
elif num1>num2 and num1>num3 and num1>num4:
    print(f"{num4} is greater than {num1,num2,num3}")

