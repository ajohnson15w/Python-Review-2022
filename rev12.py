#FUNCTIONS
def sayhi():
    print("Hello User")

sayhi()
sayhi()

def good_stuff(name):
    print("Hello " + name)

good_stuff("Fred")
good_stuff("Andy")

def mult(name, age):
    print("Hello " + name + ", you are " + str(age))

mult("Bob",46)
mult("Ted","33")

#Code that is often repeated should be put into a function.