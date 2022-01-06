#LISTS
friends = ["Kevin","Karen","Jim","Dreep","Bobert","Dreep"]

print(friends)
print(friends[0])
print(friends[2])
print(friends[-1])

friends[1]="Mike"

#grab elements starting at 1, ending up to 3
print(friends[1:3])

#LIST FUNCTIONS

lucky_numbers = [4,8,15,16,23,42]

#add on list to another
#friends.extend(lucky_numbers)

#append one item to a list
friends.append("Frank")

friends.insert(1,"Callum")

friends.remove("Jim")
print(friends)

#Pops an element off the end of the list
friends.pop()
print(friends)

print(friends.index("Kevin"))

print(friends.count("Dreep"))

friends.sort()
print(friends)

friends.reverse()
print(friends)

friends2 = friends.copy()

friends.clear()
print(friends)
print(friends2)
