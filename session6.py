import random
from decimal import *
import math

class Qualean:
    '''
    Qualean class that is inspired by Boolean+Quantum concepts. We can assign it only 3 possible real states.
    True, False, and Maybe (1, 0, -1) but it internally picks an imaginary state.
    The moment we assign it a real number, it immediately finds an imaginary number random.uniform(-1, 1)
    and multiplies with it and stores that number internally after using Bankers rounding to 10th decimal place.
    To understand this further.. imagine picking 100 times any number from 1 or 0 or -1.
    You want to store this list. But before you can store it, the quantum nature of this class is going to pick another number (random.uniform(-1, 1))
    and multiply with the number you want to store. So if I wanted to store 1, 0, 1, -1, -1.. it might get stored as 0.00123123, 0, -0.123123, 0.63463, -0.36343.
    It implements these functions (with exactly the same names)
    __and__,  __or__, __repr__, __str__, __add__, __eq__, __float__, __ge__, __gt__, __invertsign__, __le__, __lt__, __mul__, __sqrt__, __bool__
    Task is to write the above class, and then write all the functions.
    Some of the tests in the test file will check for:
    1. q + q + q ... 100 times = 100 * q
    2. q.__sqrt__() = Decimal(q).sqrt
    3. sum of 1 million different qs is very close to zero (use isclose)
    4. q1 and q2 returns False when q2 is not defined as well and q1 is False
    5. q1 or q2 returns True when q2 is not defined as well and q1 is not false
    '''
    #define constructor for Qualean class
    def __init__(self, _init_quantum_state=None):
        if _init_quantum_state and _init_quantum_state not in [-1, 0, 1]:
            raise ValueError(f"Input must be either -1,0 or 1. Entered value is : {_init_quantum_state}")
        self._init_quantum_state = 0 if _init_quantum_state == 0 else _init_quantum_state if _init_quantum_state else random.choice([-1, 0, 1])
        self.number = 0
        self.actual_quantum_gen()

    # generate imaginary part of the qualean number i.e the random decimal between -1 and 1...and return the actual qualean number after \
    # multiplying real part and imaginary part
    def actual_quantum_gen(self):
        try:
            self._init_quantum_state * Decimal(1)
        except:
            self._init_quantum_state = int(self._init_quantum_state)
        self._imag_num = Decimal(random.uniform(-1, 1))
        self.number = round(self._init_quantum_state * self._imag_num, 10)

    #return real number as per input
    def real(self):
        return self._init_quantum_state

    #return randomly generated imaginary number
    def imag(self):
        return self._imag_num

    #return final qualean number
    def qual(self):
        return self.number

    # defining object representation
    def __repr__(self):
        return 'Qualean Class Instance'

    # define return_qualean function which is a float representation rounded to 10 decimal places
    def return_qualean(self):
        return round(float(self.number),10) #float("%.10f"%self.number)

    # defining "and" operator
    # q1 and q2 returns False when q2 is not defined as well and q1 is False
    def __and__(self, other):
        if not isinstance(other, Qualean):
            return False
        if self.number == 0 or other.number == 0:
            return False
        return True

    # defining "or" operator
    # q1 or q2 returns True when q2 is not defined as well and q1 is not false
    def __or__(self, other):
        if other is not None and not isinstance(other, Qualean):
            return False
        if (self is not None and other is None) or self.number != 0 or other.number != 0:
            return True
        return False

    # define string representation of Qualean
    def __str__(self):
        return f'Qualean String for number: {str(self.number)}'

    # define add operation of either a qualean and a qualean....or a qualean and an integer/float
    def __add__(self, other):
        if isinstance(other, Qualean):
            return float(self.number + other.number)
        elif (isinstance(other,int) or isinstance(other,float)):
            return float(self.number + Decimal(other))
        else:
            raise TypeError("Invalid argument")

    # define equality operation between 2 qualean numbers
    def __eq__(self, other):
        if not isinstance(other, Qualean):
            raise TypeError(f"{other} is not of type Qualean")
        if self.number == other.number:
            return True
        else:
            return False

    # define float conversion of a qualean number
    def __float__(self):
        return float(self.number)

    # define "greater than equals to" operation between 2 qualeans
    def __ge__(self, other):
        if not isinstance(other, Qualean):
            try:
                other * 1.0
                if float(self.number) >= other:
                    return True
                else:
                    return False
            except:
                raise TypeError(f"{other} is not of type Qualean")
        if self.number >= other.number:
            return True
        else:
            return False

    # define "greater than" operation between 2 qualeans
    def __gt__(self, other):
        if not isinstance(other, Qualean):
            try:
                other * 1.0
                if float(self.number) > other:
                    return True
                else:
                    return False
            except:
                raise TypeError(f"{other} is not of type Qualean")
        if self.number > other.number:
            return True
        else:
            return False

    # define __invertsign__
    def __invertsign__(self):
        return float(self.number * -1)

    # define __invert__ ...internally calls __invertsign__
    def __invert__(self):
        return self.__invertsign__()

    # define "less than equals to" operation between 2 qualeans
    def __le__(self, other):
        if not isinstance(other, Qualean):
            try:
                other * 1.0
                if float(self.number) <= other:
                    return True
                else:
                    return False
            except:
                raise TypeError(f"{other} is not of type Qualean")
        if self.number <= other.number:
            return True
        else:
            return False

    # define "less than" operation between 2 qualeans
    def __lt__(self, other):
        if not isinstance(other, Qualean):
            try:
                other * 1.0
                if float(self.number) < other:
                    return True
                else:
                    return False
            except:
                raise TypeError(f"{other} is not of type Qualean")
        if self.number < other.number:
            return True
        else:
            return False

    # define multiplication operator between either a qualean and a qualean....or a qualean and an integer/float
    def __mul__(self, other):
        if isinstance(other, Qualean):
            return float(self.number * other.number)
        elif (isinstance(other,int) or isinstance(other,float)):
            return float(self.number * Decimal(other))
        else:
            raise TypeError("Invalid argument")

    # define square root operation of a qualean...if input value is negative, take square root of absolute value and append 'i' to it(complex)
    def __sqrt__(self):
        if self.number < 0:
            return str(round(Decimal(self.__invertsign__()).sqrt(), 10)) + 'i'
        return self.number.sqrt()

    # define boolean operator for qualean
    def __bool__(self):
        if self.number == 0:
            return False
        return True

    #return decimal implementation of qualean
    def __Decimal__(self):
        return Decimal(self.number)

    # define divmod operation of either a qualean and a qualean....or a qualean and an integer/float
    def __divmod__(self, other):
        if isinstance(other, Qualean):
            return divmod(self.number, other.number)
        elif (isinstance(other,int) or isinstance(other,float)):
            return divmod(self.number, Decimal(other))
        else:
            raise TypeError("Invalid argument")

    # define 'raise to power' operation of a qualean and an integer or float
    def __raisedtopower__(self,other):
        if (isinstance(other,int) or isinstance(other,float)):
            return self.number**other
        else:
            raise TypeError("Please enter an integer or float as the argument")

    #compare 2 non-Nan decimal instance of self and other. Return -1 if self<other, 0 if self==other and 1 if seld>other
    def __cmp__(self, other):
        if isinstance(other, Qualean):
            if self.number == other.number:
                return 0
            elif self.number < other.number:
                return -1
            else:
                return 1
        else:
            if self.number == Decimal(other):
                return 0
            elif self.number < Decimal(other):
                return -1
            else:
                return 1