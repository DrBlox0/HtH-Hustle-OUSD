# Function Basics in Python - Alvert Lin

# 1
print("- - - - -# 1: Cat Greeting Function")
def cat_greeting():
    print("Meow")

cat_greeting()

# 2
print("- - - - -# 2: Superhero Power function")
def generate_superhero_power():
    hero = "Jimmy"
    superpower = "Infinite Money"
    print(f"I am {hero}, and my superpower is {superpower}")

generate_superhero_power()


# 3 
print("- - - - -# 3: Superhero Power Function with Return")
def generate_superhero_power1():
    super_power1 = "flying"
    return super_power1

print(generate_superhero_power1())

# 4
print("- - - - -# 4: Superhero Power Function with Arguments")
def generate_superhero_power2(user_name, super_power):
    print(f"{user_name} has the super power, {super_power}")
    

generate_superhero_power2("john", "flying")

# 5 
print("- - - - -# 5: Looping through Greetings")
def cat_greetings_loop():
    for i in range(5):
        print("Meow!")
        i += 5
        

cat_greetings_loop()

# 6 
print("- - - - -# 6: Superhero Power function with Multiple Powers")
def generate_multiple_powers():
    superhero_powers = ["Flying", "Invisibility", "Super Strength"]
    for e in range(3): 
        print(superhero_powers[e])
        e += 1

generate_multiple_powers()