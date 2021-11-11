import pytest
import re
import inspect
import random
import os
import math
from decimal import *

import session6

README_CONTENT_CHECK_FOR = [
    "docstring",
    "fibonacci",
    "global",
    "nonlocal",
    "dictionary"
]


##----------------------------------tests for README file and generic tests-------------------------
def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"

def test_readme_contents():
    readme = open("README.md", "r")
    readme_words = readme.read().split()
    readme.close()
    assert len(readme_words) >= 500, "Make your README.md file interesting! Add atleast 500 words"

def test_readme_proper_description():
    READMELOOKSGOOD = True
    f = open("README.md", "r", encoding="utf-8")
    content = f.read()
    f.close()
    for c in README_CONTENT_CHECK_FOR:
        if c not in content:
            READMELOOKSGOOD = False
            pass
    assert READMELOOKSGOOD == True, "You have not described all the functions/class well in your README.md file"

def test_readme_file_for_formatting():
    f = open("README.md", "r", encoding="utf-8")
    content = f.read()
    f.close()
    assert content.count("#") >= 10

def test_indentations():
    ''' Returns pass if used four spaces for each level of syntactically \
    significant indenting.'''
    lines = inspect.getsource(session6)
    spaces = re.findall('\n +.', lines)
    for space in spaces:
        assert len(space) % 4 == 2, "Your script contains misplaced indentations"
        assert len(re.sub(r'[^ ]', '', space)) % 4 == 0, "Your code indentation does not follow PEP8 guidelines"

def test_function_name_had_cap_letter():
    functions = inspect.getmembers(session6, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"
##-------------------------------------docstring length check------------------------------------

def test_docstring_check_no_docstring():
    def foo():
        pass
    with pytest.raises(ValueError, match=r".*Function 'foo' does not have any docstring*"):
        session6.func_docstring_check(foo)

def test_docstring_check_complex():
    with pytest.raises(TypeError, match=r".*Function name passed cannot be a complex number*"):
        session6.func_docstring_check(1+2j)

def test_docstring_check_less_docstring():
    def foo():
        """
            Small docstring
        """
        pass
    with pytest.raises(ValueError, match=r".*Doctring for foo contains less than 50 characters*"):
        fn = session6.func_docstring_check(foo)
        fn()

def test_docstring_check_correct_docstring():
    fn = session6.func_docstring_check(session6.func_tracker)
    assert fn() == 193, "Docstring calculation is not correct"

def test_docstring_non_function():
    with pytest.raises(TypeError, match=r".*Function is not callable*"):
        session6.func_docstring_check("hello")


##---------------------------------------Fibonacci generator tests-------------------------------
def test_fibonacci_gen_arg_outer_func():
    with pytest.raises(TypeError, match=r".*takes 0 positional arguments*"):
        session6.func_next_fibonacci(123)

def test_fibonacci_gen_arg_inner_func():
    with pytest.raises(TypeError, match=r".*takes 0 positional arguments*"):
        s = session6.func_next_fibonacci()
        s(123)

def test_fibonacci_gen_accuracy():
    fib_sq = session6.func_next_fibonacci()
    assert (fib_sq(),fib_sq(),fib_sq(),fib_sq(),fib_sq(),fib_sq(),fib_sq()) == (0,1,1,2,3,5,8),"Fibonacci generation not correct"

##---------------------------------------function tracker - 1 -  tests------------------------------
def add(num1,num2):
    return num1+num2
def mul(num1,num2):
    return round(num1*num2,2)
def div(num1,num2):
    return round(num1/num2,2)
def sqr(num):
    return num**2

def test_func_tracker_check_add():
    func_track_obj = session6.func_tracker(add)
    assert (func_track_obj(5,6),func_track_obj(9,6),func_track_obj(1000,15)) == (11,15,1015),"Func_tracker not working correctly for add function"

def test_func_tracker_check_mul():
    func_track_obj = session6.func_tracker(mul)
    assert (func_track_obj(5,6),func_track_obj(9,6),func_track_obj(1000,15)) == (30,54,15000),"Func_tracker not working correctly for mul function"

def test_func_tracker_check_div():
    func_track_obj = session6.func_tracker(div)
    assert (func_track_obj(5,6),func_track_obj(9,6),func_track_obj(1000,15)) == (0.83,1.5,66.67),"Func_tracker not working correctly for div function"

def test_func_tracker_counter_check():
    func_add = session6.func_tracker(add)
    add1,add2,add3 = func_add(5,6),func_add(9,6),func_add(1000,15)
    func_mul = session6.func_tracker(mul)
    mul1,mul2 = func_mul(5,6),func_mul(9,6)
    func_div = session6.func_tracker(div)
    div1,div2,div3 = func_div(10,5),func_div(10,2),func_div(11,5)
    assert (session6.function_count_blank['add'], session6.function_count_blank['mul'], session6.function_count_blank['div']) == (3,2,3),"Func_tracker counter not working correctly"

def test_func_tracker_non_function():
    with pytest.raises(TypeError, match=r".*Function is not callable*"):
        session6.func_tracker("hello")

def test_func_tracker_outer_func():
    with pytest.raises(TypeError, match=r".*takes 1 positional arguments*"):
        session6.func_tracker(add,add)

def test_func_tracker_inner_func():
    with pytest.raises(TypeError, match=r".*takes 2 positional arguments*"):
        s = session6.func_tracker(add)
        s(3,5,6)
##---------------------------------------function tracker - 2 -  tests------------------------------
def test_func_tracker_update_non_function():
    func_dict = {'add':0,'mul':0,'div':0}
    with pytest.raises(TypeError, match=r".*Function is not callable*"):
        session6.func_tracker_update("hello",func_dict)

def test_func_tracker_update_check_add():
    func_dict = {'add':0,'mul':0,'div':0}
    func_track_obj = session6.func_tracker_update(add,func_dict)
    assert (func_track_obj(5,6),func_track_obj(9,6),func_track_obj(1000,15)) == (11,15,1015),"Func_tracker_update not working correctly for add function"

def test_func_tracker_update_check_mul():
    func_dict = {'add':0,'mul':0,'div':0}
    func_track_obj = session6.func_tracker_update(mul,func_dict)
    assert (func_track_obj(5,6),func_track_obj(9,6),func_track_obj(1000,15)) == (30,54,15000),"Func_tracker_update not working correctly for add function"

def test_func_tracker_update_check_div():
    func_dict = {'add':0,'mul':0,'div':0}
    func_track_obj = session6.func_tracker_update(div,func_dict)
    assert (func_track_obj(5,6),func_track_obj(9,6),func_track_obj(1000,15)) == (0.83,1.5,66.67),"Func_tracker_update not working correctly for add function"

def test_func_tracker_counter_check_counter():
    func_dict = {'add':0,'mul':0,'div':0}
    func_add = session6.func_tracker_update(add,func_dict)
    add1,add2,add3 = func_add(5,6),func_add(9,6),func_add(1000,15)
    func_mul = session6.func_tracker_update(mul,func_dict)
    mul1,mul2 = func_mul(5,6),func_mul(9,6)
    func_div = session6.func_tracker_update(div,func_dict)
    div1,div2,div3 = func_div(10,5),func_div(10,2),func_div(11,5)
    assert (func_dict['add'], func_dict['mul'], func_dict['div']) == (3,2,3),"Func_tracker_update counter not working correctly"

def test_func_tracker_counter_absent_key():
    func_dict = {'add':0,'mul':0}
    func_add = session6.func_tracker_update(add,func_dict)
    add1,add2,add3 = func_add(5,6),func_add(9,6),func_add(1000,15)
    func_div = session6.func_tracker_update(div,func_dict)
    div1,div2,div3 = func_div(10,5),func_div(10,2),func_div(11,5)
    with pytest.raises(KeyError):
        func_dict['div']
