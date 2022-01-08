#IF STATEMENTS
is_male = True
is_tall = False

if is_male and is_tall:
    print("You are male and tall")
elif is_male and not(is_tall):
    print("You are male and not tall")
elif not(is_male) and is_tall:
    print("You are tall and not male")
else:
    print("You are not both male and tall")