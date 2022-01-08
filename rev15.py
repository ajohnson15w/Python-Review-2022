#IF STATEMENTS AND COMPARISONS
def max(a, b, c):
    if a >= b and a >=c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c
        
print(max(5,3,2))

def comp_string(astr,bstr):
    if astr == bstr:
        return "Yes"
    else:
        return "No"

print(comp_string("Fruit","fruit"))
print(comp_string("eee","eee"))