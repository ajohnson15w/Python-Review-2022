#DICTIONARIES
monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",
}

print(monthConversions["Nov"])
print(monthConversions.get("Dec"))
#.get() will return a set value if the key is invalid
print(monthConversions.get("Luv"))
print(monthConversions.get("Luv", "Not a valid key"))
