#WORKING WITH STRINGS
#\n creates a new line
print("Giraffe\nAcademy")

#\" creates a new quotation mark
print("Giraffe\"Academy")

#\ creates a backslash
print("Giraffe\Academy")

phrase = "Giraffe Academy"
#Concatenation is adding things together, basically
print(phrase + " is cool")


#FUNCTIONS FOR STRINGS
print(phrase.lower())
print(phrase.upper())
print(phrase.isupper())
print(phrase.upper().isupper())
print(len(phrase))

print(phrase[0])
print(phrase[3])

print(phrase.index("a"))
print(phrase.index("Acad"))

print(phrase.replace("Giraffe", "Elephant"))