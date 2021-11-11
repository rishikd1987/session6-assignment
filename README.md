# Session 6 assignment of EPAi4.0
Scopes and Closures
***
|Name|Email|Git ID|
|----|-----|-------|
|Rishik Dutta|rishikdutta1987@gmail.com|rishikd1987|

## File Name: session6.py
***
#### Brief Description:
Aim is to write 4 functions that demonstrate effective use of scopes and closures(also known as inner functions)

#### Packages imported:
None
## Qualean class description
|Type|Name|Input parameters|Output parameters|Description|Dependency|
|----|-----|-------|-------|-------|-------|
|function|func_docstring_check|function name|inner function innercheck_docstring object|checks whether the function passed has a docstring with more than 50 characters||
|function|func_next_fibonacci|-|inner function generate_fibonacci object|generates the next fibonacci number|-|
|function|func_tracker|function name|inner function inner_tracker object|This function counts how many times a function was called. It takes a function name as input and keeps a track of how many times a function (add/mul/div) was called and updates a global dictionary variable with the counts. It uses counter as a nonlocal variable|-|
|function|func_tracker_update|function_name, dictionary|inner function inner_tracker object|similar to func_tracker but here a custom dictionary is passed which is updated with the function call counts. It uses counter as a nonlocal variable |-|

***

## File Name: test_session6.py
***
#### Brief Description:
This code is used to test the session6.py code
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
|function|test_docstring_check_no_docstring|-|-|Check for absence of docstring in a function|-|
|function|test_docstring_check_complex|-|-|Check if function name passed is a complex number instead of a proper function|-|
|function|test_docstring_check_less_docstring|-|-|Check if docstring contains less than 50 characters|-|
|function|test_docstring_check_correct_docstring|-|-|Check if function validation is able to detect presence of correct length of docstring|-|
|function|test_docstring_non_function|-|-|Check if function passed is not a valid callable function name|-|
|function|test_fibonacci_gen_arg_outer_func|-|-|Check if outer function can flag out when argument is passed|-|
|function|test_fibonacci_gen_initial_conditions|-|-|Geeric check if the first 4 fibonacci numbers are printed correctly|-|
|function|test_fibonacci_gen_arg_inner_func|-|-|Check if inner function can flag out when argument is passed|-|
|function|test_fibonacci_gen_accuracy|-|-|Check for correct fibonacci logic implementation |-|
|function|add|-|-|Custom function for addition of 2 numbers|-|
|function|mul|-|-|Custom function for multiplication of 2 numbers |-|
|function|div|-|-|Custom function for division of 2 numbers |-|
|function|sqr|-|-|Custom function for square value of a number |-|
|function|test_func_tracker_check_add|-|-|Check if func_tracker function can accurately add 2 numbers |-|
|function|test_func_tracker_check_mul|-|-|Check if func_tracker function can accurately multiply 2 numbers  |-|
|function|test_func_tracker_check_div|-|-|Check if func_tracker function can accurately divide 2 numbers  |-|
|function|test_func_tracker_counter_check|-|-|Check if func_tracker is able to correctly update function run counters in the dictionary|-|
|function|test_func_tracker_non_function|-|-|Check if func_tracker is able to correctly identify non-callable function being passed |-|
|function|test_func_tracker_outer_func|-|-|Check if func_tracker can correctly flag out 2 functions being passed to outer function at same time |-|
|function|test_func_tracker_inner_func|-|-|Check if func_tracker can correctly flag out more than 2 arguments being passed to inner function at same time|-|
|function|test_func_tracker_update_non_function|-|-|Check if func_tracker_update is able to correctly identify non-callable function being passed|-|
|function|test_func_tracker_update_check_add|-|-|Check if func_tracker_update function can accurately add 2 numbers |-|
|function|test_func_tracker_update_check_mul|-|-|Check if func_tracker_update function can accurately multiply 2 numbers|-|
|function|test_func_tracker_update_check_div|-|-|Check if func_tracker_update function can accurately divide 2 numbers  |-|
|function|test_func_tracker_counter_check_counter|-|-|Check if func_tracker_update is able to correctly update function run counters in the dictionary being passed |-|
|function|test_func_tracker_counter_absent_key|-|-|Check if func_tracker_update does not add a new key to the original dictionary being passed |-|


## Output of test in local system:
============================= test session starts =============================
platform win32 -- Python 3.7.4, pytest-5.2.1, py-1.8.0, pluggy-0.13.0 -- C:\ProgramData\Anaconda3\python.exe
cachedir: .pytest_cache
rootdir: C:\Rishik\EPAi\session6-assignment
plugins: dash-1.16.2, arraydiff-0.3, doctestplus-0.4.0, openfiles-0.4.0, remotedata-0.3.2
collecting ... collected 27 items

test_session6.py::test_readme_exists PASSED                              [  3%]
test_session6.py::test_readme_contents PASSED                            [  7%]
test_session6.py::test_readme_proper_description PASSED                  [ 11%]
test_session6.py::test_readme_file_for_formatting PASSED                 [ 14%]
test_session6.py::test_indentations PASSED                               [ 18%]
test_session6.py::test_function_name_had_cap_letter PASSED               [ 22%]
test_session6.py::test_docstring_check_no_docstring PASSED               [ 25%]
test_session6.py::test_docstring_check_complex PASSED                    [ 29%]
test_session6.py::test_docstring_check_less_docstring PASSED             [ 33%]
test_session6.py::test_docstring_check_correct_docstring PASSED          [ 37%]
test_session6.py::test_docstring_non_function PASSED                     [ 40%]
test_session6.py::test_fibonacci_gen_arg_outer_func PASSED               [ 44%]
test_session6.py::test_fibonacci_gen_arg_inner_func PASSED               [ 48%]
test_session6.py::test_fibonacci_gen_accuracy PASSED                     [ 51%]
test_session6.py::test_func_tracker_check_add PASSED                     [ 55%]
test_session6.py::test_func_tracker_check_mul PASSED                     [ 59%]
test_session6.py::test_func_tracker_check_div PASSED                     [ 62%]
test_session6.py::test_func_tracker_counter_check PASSED                 [ 66%]
test_session6.py::test_func_tracker_non_function PASSED                  [ 70%]
test_session6.py::test_func_tracker_outer_func PASSED                    [ 74%]
test_session6.py::test_func_tracker_inner_func PASSED                    [ 77%]
test_session6.py::test_func_tracker_update_non_function PASSED           [ 81%]
test_session6.py::test_func_tracker_update_check_add PASSED              [ 85%]
test_session6.py::test_func_tracker_update_check_mul PASSED              [ 88%]
test_session6.py::test_func_tracker_update_check_div PASSED              [ 92%]
test_session6.py::test_func_tracker_counter_check_counter PASSED         [ 96%]
test_session6.py::test_func_tracker_counter_absent_key PASSED            [100%]

============================= 27 passed in 0.13s ==============================

Process finished with exit code 0


