def add (x, y, *args):
    """Adds two numbers x and y and returns result.
    
    This is just an illustrative example function for a
    minimal  Python package.
    
    Args:
        x (int): an integer to be added
        y (int): a second integer to be added
        *args (list): any number of integers
    Returns:
        int : the sum of the values of x and y and those which are in *args
        
    Examples:
    
        >>> import minipy
        >>> minipy.add(1,2)
        3
        >>> minipy.add(3,4,5,6)
        18
        
    """
    z=x+y
    for n in args:
        z += n
    return(z)
    
