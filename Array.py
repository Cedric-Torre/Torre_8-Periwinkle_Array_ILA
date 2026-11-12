Fruits = []
print("Hey I'm lowk craving fruit, let's go to the market to buy")
print("Hey we're at the market")
Fruits.append(input("Buy me a fruit, I'm poor:"))

while len(Fruits) < 5:
    Fruits.append(input("Buy me one more fruit:"))
else:
    print("That's enough I can't eat it all!")
    for i in range(5):
        print(Fruits[i])

print("Hey can you change atleast one I don't like them.")
index = int(input("Input Index to Update[0-4]:"))
new = input("Input New Value:")
Fruits[index] = new

slice1 = int(input("Enter Slice Range 1:"))
slice2 = int(input("Enter Slice Range 2:"))
sub_list = Fruits[slice1:slice2]
print(f"Sliced List: [{slice1}:{slice2}] {sub_list}")

search = input("Which one is your favorite fruit? Let's search for it in the sliced list and I'll give it to you because I feel bad:")
if search in sub_list:
    print(f"Fruit {search} found!")
else:
    print(f"Fruit {search} not found")

print(f"Here is your updated original list {Fruits}, I'm not hungry anymore")
print(f"And here is your sliced list {sub_list}")