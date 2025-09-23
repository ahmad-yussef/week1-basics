#conditionals.py - Day 2: if/ elif/ else examples

#example 1: basic if/else
age = int(input("How old are you? "))
if age >= 18:
    print("You are an adult.")
elif age < 18 :
    print("You are a minor.")



#example 2: Grade to letter
grade = int(input("Enter your grade (0-100)"))
if grade >= 90:
    print("A")
elif grade >=80:
    print("B")
elif grade >= 70:
    print("C")
else:
    print("F")


#example 3: password check
password = input("Enter password: ")
if password == "secret123":
    print("Access granted")
else:
    print("Access denied")



