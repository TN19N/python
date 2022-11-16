def what_are_the_vars(*args, **kargs): 
    """
        args :
            *args any number of arguments
            **kargs any number of key, value arguments
        return :
            return an Object of class (ObjectC) with this arguments as
            attributes (*args take a key with saffix [var_{0, 1, ...}])
            return None if tow attributes added with the same key
    """
    obj = ObjectC()

    for key, value in kargs.items() :
        setattr(obj, key, value)

    prefex = 0
    for element in args :
        if f'var_{prefex}' in kargs :
            return None
        else :
            setattr(obj, f'var_{prefex}', element)
        prefex += 1

    return obj

class ObjectC(object):

    def __init__(self):
        pass

def doom_printer(obj): 
    if obj is None:
        print("ERROR") 
        print("end") 
        return
    for attr in dir(obj):
        if attr[0] != '_':
            value = getattr(obj, attr) 
            print("{}: {}".format(attr, value))
    print("end")

if __name__ == "__main__":
    obj = what_are_the_vars(7)
    doom_printer(obj)
    obj = what_are_the_vars(None, [])
    doom_printer(obj)
    obj = what_are_the_vars("ft_lol", "Hi")
    doom_printer(obj)
    obj = what_are_the_vars()
    doom_printer(obj)
    obj = what_are_the_vars(12, "Yes", [0, 0, 0], a=10, hello="world")
    doom_printer(obj)
    obj = what_are_the_vars(42, a=10, var_0="world")
    doom_printer(obj)
    obj = what_are_the_vars(42, "Yes", a=10, var_2="world")
    doom_printer(obj)