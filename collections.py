# as well as the simple data types Python has collections
a = 1
b = 'words'
c = 3.14
d = True

# lists can contain any data types. Ordinal counting from zero
things_list = [42, 'wow', None, a, d, b, c]
things_list.pop() # removes from the RIGHT
things_list.append( [5,4,3] ) # adds to the RIGHT
# lists are mutable
things_list[3] = 'altered'
print(things_list[1:6:2]) # start:stop-before:step

# tuple
my_tuple = (b, a, c, True, 'immutable', things_list) # tuples are immutable
# my_tuple[0] = 'oops'
for item in my_tuple:
    print(item)

# string - an ordinal immutable collection of characters
s = 'strings are immutable'
# s[3] = 'X' # nope
print(s[4:12:3])
 
# dictionary (mutable)
d = {'name':'Floella', 'age':72, 'airtime':1967}
d['hero'] = True
# d.hero = False # nope
print(d)

# so whats going on??
t = ('oobly', 'woobly')
o, w = t
print(o, w)

# dictionary is made up of key-value pairs
# Question - what's going on with this 'in' loop..?
for k, v in d.items(): # dictionary is iterable
    print(k, v)

# fun with casting types
codes_str = 'ATVI, ADBE, AAPL, BA, CPB, DAL, EA, EL, GPS, INTC, MRK, NFLX, NVDA, PFE, RHT, UA'
names_str = 'Activision, Adobe, Apple, Boeing, Campbell Soup, Delta Air Lines, Electronic Arts, Gap, Intel, Merk, Netflix, Nvidia, Pfizer, Red Hat, Under Armour'
# print(codes_str[2:18:2])
code_l = codes_str.split(', ')
names_l = names_str.split(', ')
print(names_l)

# Python has a 'zip' operator
stock = dict( zip(code_l, names_l) ) # cast our zip object as a dictionary
print(stock)