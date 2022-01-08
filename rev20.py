#FOR LOOP
#for loops let us iterate over specific things
for letter in "Moo":
    print(letter)
friends = ["Jim","Karen","Kevin"]
for friend in friends:
    print(friend)
for index in range(5):
    print(index)

food = ["butter","cheese","apple"]
for index in range(len(food)):
    print(food[index])

for index in range(5):
    if index == 0:
        print("First iteration")
    else:
        print("Not first")