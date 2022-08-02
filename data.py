# we may grab data from....
# a database
# an API e.g. https://ooblywooby.com
# python start-up variable
# read/write files (any file)
# when we look at Data Analysis we will open csv and xlsx
# sensors, e.g. temperature, motion ...
# user input

c_str = input('Stock Code: ') # EVERY input is ALWAYS a string
print(c_str, type(c_str), c_str.isnumeric() )

invalidQty = True
while invalidQty:
    q_str = input('Stock Quantity: ')
    if q_str.isdecimal():
        q_int = int(float(q_str)) # good practice
        invalidQty = False # fix this!!!!!
    break