# Lab 3: ALvert Lin

# Strings = ""
# Lists = []
# Dictionaries = {}

# Strings ----------

print("-------Strings_Task1-------")
foods = "Sushi, Udon, Pizza" #1

print(foods[0:3]) # 2 slicing
print(foods[-3:]) # 3
print(foods[0]+foods[-1]) # 4
x = foods.split()
print(x) # 5
print("".join(foods)) # 6

# Lists ------------

print("-------Lists_Task2-------")

number_list = [1, 2, 3, 4, 5] # 1
number_list.append(11) # 2 
print(number_list)
number_list.insert(3, "yellow") # 3
print(number_list)
number_list.pop(-1) # 4
print(number_list)
number_list.remove(2) # 5
print(number_list)
print(number_list[0:3]) # 6
print(number_list[-3:]) # 7

# Dictionary ---------

print("--------Dictionary_Task3-------")

books = {"Dav Pilkey": "Dog Man", "Neal Shushterman": "Challenger Deep", "author3": "book1", "author4": "book2"} # 1
a = books.keys() # 2
print(a)
b = books.values() # 3
print(b)
c = books.get("Dav Pilkey") # 4
print(c)
books.pop("author3") # 5 
print(books)
del books["Dav Pilkey"] # 6
print(books)






