#while loops:

count = 1
while count <= 5:
    print("Count is:", count)
    count+=1

#when do we use f-string? when we want to control exactly how the text looks

name = "Jacob"
age = 22
height = 191.2 

print(f"Name: {name}, Age: {age}, Height: {height}meters")


#for loops:

for i in range(1,6):
    print(f"Number: {i}")


names = ["Rupert", "Jacob", "Jay"]
for name in names:
    print(f"Hello, {name}!")

#in the loop below, we are testing how a for loop takes each element from a list, put it in variable n, runs the code inside the loop, then move to the next element in the list.
#python sees (continue), stops running the rest of the code in that loop body for the current element, jumps to the next iteration.
numbers = [1,2,3,4,5]
for n in numbers:
    if n == 3:
        print("Skipping 3...")
        continue #skip this loop when n = 3
    if n ==5:
        print("Found 5, stopping loop!")
        break
    print(f"Number is {n}")


#lets try range() and nested loop
#think of it as a clock where the outer loop is the hours hand, inner loop is the minutes hand, the outer loop runs once, helping the inner loop to run its whole body code, then the ojuter loop's second iteration comes in.. and so on. 


for i in range(1, 4):
    for j in range (1, 5):
        print(f"{i} * {j} = {i*j}")

    print("-----")

#looping with range, below is a range with step

for i in range (0 , 15 , 3):
    print(i)

#looping over strings

name = "Ahmad"

for char in name:
    print(char)

#enumerate

students = ["Ahmad", "Ali", "Sarah"]
for i, name in enumerate(students):
    print(f"Student {i+1}: {name}")

#test 1
back = "backend"

for i, name in enumerate(back):
    if name == "e":
         continue
    if name == "n":
        print("Found n, stopping loop")
        break
    print(f"index: {i}, Character: {name}")