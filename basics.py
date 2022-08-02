# variables, simple types, basic mathematics

a = True # False, also None
b = 'hello'
b = 0.3 #BODMAS
print(type(b))
c = 1 # int
print ( type(b+c))
print(b**0.5)

# conditionals
if b > 1: # > < == >= etc..
    print('b is greater than 1') # indentation matters
    # could do ther stuff
elif b<0: # else if
    print('b is negative')
    pass # does nothing
else:
    print('b is not negative but is less than or equal 1')
# a block ends when we no longer indent the code

for i in range(1,10,3): # range start, stop-before, step
    print(i*i)