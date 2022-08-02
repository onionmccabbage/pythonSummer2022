# does not work
import doctest

def cube(x):
    """
    The cube function returns x*x*x
    >>> cube(3)
    27
    >>> cube(-1)
    -1
    """
    return x*x*x



def pythag(x=3, y=4):
    '''
    Documentation String (docstring)
    Take x and y (representing lengths of sides of a right-angled triangle)
    Return the hypotenuse
    >>> pythag(-3, -4)
    >>> 5.0
    '''
    return ((x*x)+(y*y))**0.5 # return square root of sum of squares

# h = pythag()
# print(h)

if __name__ == '__main__':
    doctest.testmod(verbose=True) # we want to see all the info