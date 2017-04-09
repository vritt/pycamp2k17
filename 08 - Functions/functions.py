

# Function definition is here
def printme(string, string2="!"):
    """This prints a passed string  into this function"""
    print(string, string2)


def addme(firstparam, secondparam=None, *args, **mydict):
    """[summary]

    [description]

    Arguments:
        firstparam {[type]} -- [description]
        *args {[type]} -- [description]
        **mydict {[type]} -- [description]

    Keyword Arguments:
        secondparam {[type]} -- [description] (default: {None})
    """
    print(firstparam)
    print(secondparam)
    print(args)
    print((mydict))


def addtwo():
    print(3 + 5)


'''
# Now you can call printme function
printme("This is first call to the user defined function!")
printme("Again second call to the same function")

printme('My Name', string2="9")

addtwo()
'''
if __name__ == '__main__':

    addme(1, 12, 4, 5, 6)
