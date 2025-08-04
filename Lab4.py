Checking = "yes"

while Checking == "yes": 
  print("what is your age")
  user_input = input()
    
  if int(user_input) >= 18:
      print("yes you can vote")
      break
  elif int(user_input) < 18:
     print("You are not old enough")
     break
  

list1 = [3, -1, 0, 6, -4]

for x in list1:
    if x > 0:
        print("value is positive")
    elif x < 0: 
        print("value is negative")
    else:
         print("number is zero")


inventory = ["tnt", "glass", "grass", "bedrock", "End Crystal", "netherite"]

for i in inventory:
    if i == "bedrock":
        print("why do you have this in your inventory?")
    elif i == "tnt":
        print("Go bomb a House")


for i in inventory: 
    if i == "netherite":
        print("Metal")
    elif i == "tnt":
        print("boom")









