student_1 = {
    "name": "John",
    "age": 16,
    "class": 9
}

student_2 = {
    "name": "Alice",
    "age": 15,
    "class": 10
}

# Accessing dictionary item

# Find name of student 2

print(f" The name of student-2 is {student_2['name']}")

# find age of student 1

print(f"The Age of student 1 is { student_1['age']}")


# 3 scenaios of retreival from dictionary

# 1st Scenario: Retreive both Key and value

for my_key, my_value in student_1.items():
    print (f"The key is {my_key}, and the value is {my_value}")

# 2nd scenario: retreive only Keys

for my_key in student_1.keys():
    print (f"The key is {my_key}")

# 3rd scenario: retreive only values

for my_value in student_1.values():
    print(f" The value is {my_value}")


# Add a new key-value pair to a dictionary
print ("Added a new key-value pair to student_1")
student_1["address"] = "srinagar"

print(student_1)

# Update an existing key

print ("Modified existing key class to 10th")
student_1["class"] = 10

print(student_1)

# Multiple updates on dictionary

print("Making multiple updates on dictionary")
student_1.update({"class": 11, "age": 18, "address": "jammu"})

print(student_1)

student_1.update({"phone": "600121232"})
print ("Updated phone number")
print(student_1)


#Removing key-value pairs

# pop() : removes a key-value pair and returns its value 
old_phone_no = student_1.pop("phone") 
print(f"The phone number {old_phone_no} was removed")
print(student_1)


# popitem() : removes last key-value pair of dictionary

student_1.popitem()
print("Using popitem, last key-value pair will be removed")
print(student_1)

# clear() : empties whole dictionary

student_1.clear()
print("Student_1 dictionary is cleared")

print(student_1)
st2_name=student_2.get("name")
print(st2_name)

print(f"The age of student_2 is {student_2.get('age')}")