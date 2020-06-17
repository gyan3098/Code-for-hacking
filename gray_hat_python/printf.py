#Py -2 printf.py
from ctypes import *

# mvscrt = cdll.mvscrt
# message_string = "Hello Gyan!\n"
# mvscrt.printf("Testing: %s",message_string)

a = c_char_p("loves the python")
print(a.value)            # dereferncing a pointer


## Defining structures 

class beer_recipe(Structure):
    _fields_ = [
        ("amt_barley",c_int),
        ("amt_water",c_int)
    ]

print(beer_recipe.amt_barley)

## Defining unions
class barley_amount(Union):
    _fields_ = [
        ("barley_long",c_long),
        ("barley_int",c_int),
        ("barley_char",c_char*8)
    ]

value = raw_input("Enter the amount of barley to put into the beer vat:") 
my_barley = barley_amount(int(value)) 
print "Barley amount as a long: %ld" % my_barley.barley_long 
print "Barley amount as an int: %d" % my_barley.barley_long 
print "Barley amount as a char: %s" % my_barley.barley_char
