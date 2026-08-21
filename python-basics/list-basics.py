
colors = ["red", "green", "yellow"]
scores = [60, 45, 95, 77, 58, 23, 78, 99, 23, 99, 32, 99]

# Accessing list items:
#1. Using index 0...<last>
#2. Negative index -1 = last-item

print (f" Third color is {colors[2]}")
print (f" last score value is {scores[-1]}")


#Various methods to add utems to list

# 1. Append
colors.append("teal")
print (colors)

#2. Insert

colors.insert(1, "purple")
print (colors)

#3. Extend

modern_colors = ["oak", "petrol-blue"]

colors.extend(modern_colors)
print (colors)


## Removing items from list

# 1. remove
colors.remove("oak")
print (colors)

# 2. pop
colors.pop() # default last item will be removed
print(colors)

colors.pop(2)
print(colors)

# 3. clear

colors.clear()
print ("Printing after clearing colors...")
print (colors)


## Useful list operations

# 1. count
print ("Below no. of students have obtained 99 marks")
print (scores.count(99)) # How many have 99 marks


#2. index

print (f"The index of score 77 is {scores.index(77)}")

# 3.sort

scores.sort()
print(scores)

scores.sort(reverse=True)
print(scores)
# 4. reverse

scores.reverse()
print(scores)

print (f"The length of list scores is {len(scores)}")