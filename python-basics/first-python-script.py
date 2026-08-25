#!/opt/homebrew/bin/python3
print ("Hello-World")
name = "python-teacher"
age = 30

# If- Else Statements

if age >= 20:
  print("Status: You are eligible")
else:
  print("Status: You are not eligible. You need to be 20 yrs or above")


#User-input
new_age = int(input("What is your new age:"))

if new_age >= 18:
  print ("You are eligible")
else:
  print ("Your are not eligible")


#List 
fruits = ["apple", "banana", "avocado", "cherry", "watermelon"]

#For loop

for fruit in fruits:
  print(fruit)

print (f" The second item in fruits list is {fruits[1]}")  


# While loop

count = 3

while count > 0:
  print (f"{count}..")
  count -= 1

