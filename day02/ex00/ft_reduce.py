def ft_reduce(function_to_apply, iterable):
    """Apply function of two arguments cumulatively. 
    Args:
        function_to_apply: a function taking an iterable.
        iterable: an iterable object (list, tuple, iterator).
    Return:
        A value, of same type of elements in the iterable parameter.
        None if the iterable can not be used by the function.
    """

    try:
        iter(iterable)
    except:
        raise TypeError('ft_reduce() arg 2 must support iteration')

    if len(iterable) == 0 :
        raise TypeError('ft_reduce() of empty sequence with no initial value')

    res = None
    for element in iterable:
        if res is None :
            res = element
        else:
            res = function_to_apply(res, element)
    return res