def suma(a, b):
    '''
    Suma dos números
    >>> suma(2, 3)
    5
    >>> suma(2, -3)
    -1
    >>> suma(-2, -3)
    -5
    >>> suma(0, 0)
    0
    >>> suma(0, 3)
    3
    >>> suma(3, 0)
    3
    '''
    return a + b

def resta(a, b):
    '''
    Resta dos números
    >>> resta(2, 3)
    -1
    >>> resta(2, -3)
    5
    >>> resta(-2, -3)
    1
    >>> resta(0, 0)
    0
    >>> resta(0, 3)
    -3
    >>> resta(3, 0)
    3
    '''
    return a - b

def multiplicacion(a, b):
    '''
    Multiplica dos números
    >>> multiplicacion(2, 3)
    6
    >>> multiplicacion(2, -3)
    -6
    >>> multiplicacion(-2, -3)
    6
    >>> multiplicacion(0, 0)
    0
    >>> multiplicacion(0, 3)
    0
    >>> multiplicacion(3, 0)
    0
    '''
        
    return a * b
  
def division(a, b):
    '''
    Divide dos números
    >>> division(0, 0)
    Traceback (most recent call last):
    ValueError: No se puede dividir por cero
    '''
    if b!=0:
        '''
        Divide dos números
        >>> division(2, 3)
        2/3
        >>> division(2, -3)
        2/-3
        >>> division(-2, -3)
        -2/-3
        >>> division(0, 0)
        0/0
        >>> division(0, 3)
        0/3
        >>> division(3, 0)
        3/0
        '''
        
        return a / b
    else:
        raise ZeroDivisionError("No se puede dividir por cero")

