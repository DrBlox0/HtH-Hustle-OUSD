# CRUD Activity: Create, Read, Update and Destroy - Alvert Lin - 07/19/25


cookbook = [] # Step 1 - cookbook = (Empty LIST)

def create(*recipe): # Step 2 - Create a function named (create) and parameter is (recipe)
    cookbook.extend(recipe)
    print(f"{recipe} has been added to your cookbook ")

#create("brownies", "pizza", "udon")

def read(index): 
    if index < len(cookbook):
      item = cookbook[index]
      print(f"the recipe at index {index} is: {item}")
    else:
      print("Sorry this index is out of bounds")

#read(1)
              
def update(index, recipe):
    if index < len(cookbook):
      cookbook[index] = recipe
      print(f"The index {index} has been updated to {recipe} ")
    else:
      print("The index is out of bounds, please choose another position ")
#update(0, "chicken")

#print(cookbook)

def destroy(index):
    if index < len(cookbook):
      item = cookbook.pop(index)
      print(f"{item} recipe at index {index} has been removed. ")
    else:
       print("index is out of bounds, please choose another position")

#destroy(0)

def list_all_recipes():
   for recipe in cookbook:
      print(recipe)

#list_all_recipes()

def main():
    while True:
        print("\nCookbook Recipes")
        print("1. Add a Recipe")
        print("2. Read a Recipe")
        print("3. Update a Recipe")
        print("4. Delete a Recipe")
        print("5. Display all Recipes")
        print("6. Exit")


        choice = input("Choose an option (1-6): ")


        if choice == "1":
            recipe = input("Enter the name of the recipe: ")
            create(recipe)
        elif choice == "2":
            index = input("Enter the index of the recipe to read: ")
            index = int(index)
            read(index)
        elif choice == "3":
            index = input("Enter the index of the recipe to update: ")
            recipe = input("Enter the name of the recipe you want to update it with: ")
            index = int(index)
            update(index, recipe)
        elif choice == "4":
            index = input("Enter the index of the recipe to delete: ")
            index = int(index)
            destroy(index)
        elif choice == "5":
            list_all_recipes()
        elif choice == "6":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice, please try again.")


main()



