
function_count_blank = {}

def func_docstring_check(func):
    """
        func_docstring_check is a closure that takes a function and then checks whether the function passed
        has a docstring with more than 50 characters
    """
    docstring_count = 50
    #Validations
    if type(func) is complex:
        raise TypeError(f"Function name passed cannot be a complex number. Function Name provided: {func}")
    if not callable(func):
        raise TypeError("Function is not callable")
    if func.__doc__ is None:
        raise ValueError(f"Function '{func.__name__}' does not have any docstring")
    def innercheck_docstring():
        nonlocal func
        #check docstring
        length_doc_str = len(func.__doc__.replace("\n","").replace(" ",""))
        if length_doc_str < docstring_count:
            raise ValueError(f"Doctring for {func.__name__} contains less than 50 characters")
        else:
            return length_doc_str
    return innercheck_docstring

def func_next_fibonacci():
    """
        func_next_fibonacci is a closure that gives the next Fibonacci number. Each invokation returns
        the next number in the fibonacci series
    """
    num1 = 0
    num2 = 1
    counter = 0
    def generate_fibonacci():
        nonlocal num1, num2, counter
        if counter == 0:
            counter += 1
            return num1
        elif counter == 1:
            counter += 1
            return num2
        else:
            counter += 1
            num3 = num1 + num2
            num1, num2 = num2, num3
            return num3
    return generate_fibonacci

def func_tracker(fn):
    """
        func_tracker is a closure that counts how many times a function was called. It takes a function name as
        input  keep a track of how many times a function (add/mul/div) was called and updates
        a global dictionary variable with the counts
    """
    counter = 0
    global function_count_blank
    #validation
    if not callable(fn):
        raise TypeError("Function is not callable")
    def inner_tracker(*args,**kwargs):
        nonlocal counter
        counter += 1
        function_count_blank[fn.__name__] = counter
        return fn(*args,**kwargs)

    return inner_tracker



def func_tracker_update(fn,counter_dict=dict()):
    """
        func_tracker_update is similar to func_tracker but here a custom dictionary is passed which is updated
        with the function call counts
    """
    counter = 0
    global function_count
    if not callable(fn):
        raise TypeError("Function is not callable")
    def inner_tracker(*args,**kwargs):
        nonlocal counter
        counter += 1
        if fn.__name__ in list(counter_dict.keys()):
            counter_dict[fn.__name__] = counter
        return fn(*args,**kwargs)

    return inner_tracker







