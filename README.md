# Session 4 assignment of EPAi4.0
Numeric Types II
***
|Name|Email|Git ID|
|----|-----|-------|
|Rishik Dutta|rishikdutta1987@gmail.com|rishikd1987|

## File Name: session4.py
***
#### Brief Description:
Aim is to write a Qualean class that is inspired by Boolean+Quantum concepts. We can assign it only 3 possible real states. True, False, and Maybe (1, 0, -1) but it internally picks an imaginary state. The moment you assign it a real number, it immediately finds an imaginary number random.uniform(-1, 1) and multiplies with it and stores that number internally after using Bankers rounding to 10th decimal place. To understand this further.. imagine picking 100 times any number from 1 or 0 or -1. You want to store this list. But before you can store it, the quantum nature of this class is going to pick another number (random.uniform(-1, 1)) and multiply with the number you want to store. So if I wanted to store 1, 0, 1, -1, -1.. it might get stored as 0.00123123, 0, -0.123123, 0.63463, -0.36343. 
* It implements these functions (with exactly the same names)
__and__,  __or__, __repr__, __str__, __add__, __eq__, __float__, __ge__, __gt__, __invertsign__, __le__, __lt__, __mul__, __sqrt__, __bool__

* Some of the tests in the test file will check for:
	* q + q + q ... 100 times = 100 * q
	* q.__sqrt__() = Decimal(q).sqrt
	* sum of 1 million different qs is very close to zero (use isclose)
	* q1 and q2 returns False when q2 is not defined as well and q1 is False
	* q1 or q2 returns True when q2 is not defined as well and q1 is not false
#### Packages imported:
* random
* decimal
* math
* numpy
## Qualean class description
|Type|Name|Input parameters|Output parameters|Description|Dependency|
|----|-----|-------|-------|-------|-------|
|function - constructor|__init__|initial quantum state as a real number(default - None)|None|checks if value either -1, 0 or 1. If None entered, it will select a random integer among -1, 0 or 1. It will then call actual_quantum_gen() to generate the final quantum number to be stored|actual_quantum_gen()|
|function|actual_quantum_gen|-|Decimal|multiplies the real initial quantum number with a random generated decimal number between -1 and 1 to give the final quantum state|-|
|function|real|self|int|Returns the initial quantum state as the real value(-1, 0 or 1)|-|
|function|imag|self|Decimal|returns the random value between -1 and 1 that is multiplied with the real number to generate the final Qualean value |-|
|function|qual|self|Decimal|returns the final qualean value as Decimal|-|
|function|__repr__|-|string|States that it is a qualean class instance|-|
|function|return_qualean|-|float|returns the float64 representation of the final quantum state|-|
|function|__and__|qualean(q1),qualean(q2)|boolean|q1 and q2 returns False when q2 is not defined as well and q1 is False|-|
|function|__or__|qualean(q1),qualean(q2)|boolean|q1 or q2 returns True when q2 is not defined as well and q1 is not false|-|
|function|__str__|-|string|returns text as "Qualean String for number: {q}"|-|
|function|__add__|qualean,qualean|float|summation of the qualean numbers|-|
|function|__eq__|qualean,qualean|boolean|check equality of 2 qualean numbers|-|
|function|__float__|-|float|check equality of 2 qualean numbers|-|
|function|__ge__|qualean(q1),qualean(q2)|boolean|check whether q1 >= q2|-|
|function|__gt__|qualean(q1),qualean(q2)|boolean|check whether q1 > q2|-|
|function|__le__|qualean(q1),qualean(q2)|boolean|check whether q1 <= q2|-|
|function|__lt__|qualean(q1),qualean(q2)|boolean|check whether q1 < q2|-|
|function|__invertsign__|self|float|invert sign of q|-|
|function|__invert__|self|float|invert sign of q|-|
|function|__mul__|qualean(q1),qualean/decimal(q2)|float|product of q1 and q2|-|
|function|__sqrt__|qualean(q)|float/imaginary(string)|square root of the qualean number - float if q is +ve, imaginary if q is -ve|-|
|function|__bool__|qualean(q)|boolean|False if 0 else True|-|
|function|__Decimal__|self|Decimal|returns decimal value of qualean number|-|
|function|__divmod__|self,other|tuple|uses divmod method to generate a tuple of quotient and reminder after division of self.number and other|-|
|function|__raisedtopower__|self,other|float|self.number raised to the power of 'other'|-|
|function|__cmp__|self,other|int|compare 2 non-Nan decimal instance of self and other. Return -1 if self<other, 0 if self==other and 1 if seld>other|-|

***

## File Name: test_session4.py
***
#### Brief Description:
This code is used to test the session4.py code
#### Packages imported:
* pytest
* random
* string
* os
* re
* inspect
* math
* decimal


|Type|Name|Input parameters|Output parameters|Description|Dependency|
|----|-----|-------|-------|-------|-------|
|function|test_readme_exists|-|-|Check if README.md file exists|-|
|function|test_readme_contents|-|-|Check if README.md file contains atleast 500 words|-|
|function|test_readme_proper_description|-|-|Check if all functions/classes have been described in README.md file|-|
|function|test_readme_file_for_formatting|-|-|Check for formatting in README.md file |-|
|function|test_indentations|-|-|Check for misplaced indentations |-|
|function|test_function_name_had_cap_letter|-|-|Check for upper case characters in function names |-|
|function|test_qualean_repr|-|-|Check for correct representation of the Qualean object|-|
|function|test_qualean_str|-|-|Check if the Qualean object is printed as a correct string|-|
|function|test_function_qualean_type|-|-|Check for Qualean type |-|
|function|test_qualean_decimal_precision|-|-|Check whether rounding to 10 decimal places is happening for return_qualean() method|-|
|function|test_function_count|-|-|Check if there are more than 25 methods in the Qualean class definition|-|
|function|test_function_repeatations|-|-|Check if 2 or more than 2 functions have same name |-|
|function|test_100_qualeans|-|-|Check if sum of a qualean 100 times is equivalent to 100 * qualean|-|
|function|test_function_sqrt|-|-|Check for correct square root implementation |-|
|function|test_million_qualeans_sum|-|-|Check if the sum of a qualean a million time is very close to zero |-|
|function|test_million_qualeans_mul|-|-|Check if the product of a qualean a million time is very close to zero |-|
|function|test_qualean_valid_input|-|-|Check if wrong input of real values raises ValueError |-|
|function|test_invalid_input_valueerror_provides_relevant_message|-|-|Check if ValueError contains correct message |-|
|function|test_qualean_validity|-|-|Check if generated value is a correct qualean object and if value lies between -1 and 1 |-|
|function|test_function_and|-|-|Check for correct AND operation between 2 qualeans |-|
|function|test_and_q_notdefined|-|-|Check if correct AND operation is implemented if 2nd value is None |-|
|function|test_and_q_false|-|-|Check if correct AND operation is implemented if 1st value is False |-|
|function|test_function_or|-|-|Check for correct OR operation between 2 qualeans |-|
|function|test_or_q_notdefined|-|-|Check if correct OR operation is implemented if 2nd value is None |-|
|function|test_or_q_false|-|-|Check if correct OR operation is implemented if 1st value is False |-|
|function|test_function_add|-|-|Check for addition of 2 qualeans |-|
|function|test_function_add_non_qualean|-|-|Check for correct addition of a Qualean and float value |-|
|function|test_function_mul|-|-|Check for multiplication of 2 Qualeans|-|
|function|test_function_mul_non_qualean|-|-|Check for correct multiplication of a Qualean and float value  |-|
|function|test_function_ge|-|-|Check for correct greater than equals to operation between 2 Qualeans |-|
|function|test_function_ge_non_qualean|-|-|Check for correct greater than equals to operation between a Qualean and non-qualean |-|
|function|test_function_gt|-|-|Check for correct greater than operation between 2 Qualeans |-|
|function|test_function_gt_non_qualean|-|-|Check for correct greater than operation between a Qualean and non-qualean |-|
|function|test_function_le|-|-|Check for correct lesser than equals to operation between 2 Qualeans |-|
|function|test_function_le_non_qualean|-|-|Check for lesser than equals to operation between a Qualean and non-qualean |-|
|function|test_function_lt|-|-|Check for correct lesser than operation between 2 Qualeans |-|
|function|test_function_lt_non_qualean|-|-|Check for lesser than operation between a Qualean and non-qualean |-|
|function|test_function_with_non_number|-|-|Check for correct exception handling in case of add,multiplication, equals to etc operation between qualean and string value |-|
|function|test_function_bool|-|-|Check for correct boolean representation implementation |-|
|function|test_function_eq|-|-|Check for equality between 2 qualeans |-|
|function|test_function_float|-|-|Check for correct float representation implementation  |-|
|function|test_function_invertsign|-|-|Check for correct reverse sign implementation  |-|





## Output of test in local system:
============================= test session starts =============================
platform win32 -- Python 3.7.4, pytest-5.2.1, py-1.8.0, pluggy-0.13.0 -- C:\ProgramData\Anaconda3\python.exe
cachedir: .pytest_cache
rootdir: C:\Rishik\EPAi\session-4-rishikd1987
plugins: dash-1.16.2, arraydiff-0.3, doctestplus-0.4.0, openfiles-0.4.0, remotedata-0.3.2
collecting ... collected 42 items

test_session4.py::test_readme_exists PASSED                              [  2%]
test_session4.py::test_readme_contents PASSED                            [  4%]
test_session4.py::test_readme_proper_description PASSED                  [  7%]
test_session4.py::test_readme_file_for_formatting PASSED                 [  9%]
test_session4.py::test_indentations PASSED                               [ 11%]
test_session4.py::test_function_name_had_cap_letter PASSED               [ 14%]
test_session4.py::test_qualean_repr PASSED                               [ 16%]
test_session4.py::test_qualean_str PASSED                                [ 19%]
test_session4.py::test_function_qualean_type PASSED                      [ 21%]
test_session4.py::test_qualean_decimal_precision PASSED                  [ 23%]
test_session4.py::test_function_count PASSED                             [ 26%]
test_session4.py::test_function_repeatations PASSED                      [ 28%]
test_session4.py::test_100_qualeans PASSED                               [ 30%]
test_session4.py::test_function_sqrt PASSED                              [ 33%]
test_session4.py::test_million_qualeans_sum PASSED                       [ 35%]
test_session4.py::test_million_qualeans_mul PASSED                       [ 38%]
test_session4.py::test_qualean_valid_input PASSED                        [ 40%]
test_session4.py::test_invalid_input_valueerror_provides_relevant_message PASSED [ 42%]
test_session4.py::test_qualean_validity PASSED                           [ 45%]
test_session4.py::test_function_and PASSED                               [ 47%]
test_session4.py::test_and_q_notdefined PASSED                           [ 50%]
test_session4.py::test_and_q_false PASSED                                [ 52%]
test_session4.py::test_function_or PASSED                                [ 54%]
test_session4.py::test_or_q_notdefined PASSED                            [ 57%]
test_session4.py::test_or_q_false PASSED                                 [ 59%]
test_session4.py::test_function_add PASSED                               [ 61%]
test_session4.py::test_function_add_non_qualean PASSED                   [ 64%]
test_session4.py::test_function_mul PASSED                               [ 66%]
test_session4.py::test_function_mul_non_qualean PASSED                   [ 69%]
test_session4.py::test_function_ge PASSED                                [ 71%]
test_session4.py::test_function_ge_non_qualean PASSED                    [ 73%]
test_session4.py::test_function_gt PASSED                                [ 76%]
test_session4.py::test_function_gt_non_qualean PASSED                    [ 78%]
test_session4.py::test_function_le PASSED                                [ 80%]
test_session4.py::test_function_le_non_qualean PASSED                    [ 83%]
test_session4.py::test_function_lt PASSED                                [ 85%]
test_session4.py::test_function_lt_non_qualean PASSED                    [ 88%]
test_session4.py::test_function_with_non_number PASSED                   [ 90%]
test_session4.py::test_function_bool PASSED                              [ 92%]
test_session4.py::test_function_eq PASSED                                [ 95%]
test_session4.py::test_function_float PASSED                             [ 97%]
test_session4.py::test_function_invertsign PASSED                        [100%]

============================= 42 passed in 23.67s =============================

Process finished with exit code 0

