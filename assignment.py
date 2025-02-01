def format_string(name, age):
    """
    Create a formatted string using f-strings.
    Args:
        name (str): Person's name
        age (int): Person's age
    Returns:
        str: Formatted string
    """
    formattedString = f"My name is {name} and I am {age} years old"
    return formattedString

    pass

def conditional_check(number):
    """
    Check if a number is greater, lesser, or equal to 10.
    Args:
        number (int): Number to check
    Returns:
        str: "Greater", "Lesser", or "Equal"
    """

    if number>10:
        return "Greater"
    elif number <10:
        return "Lesser"
    elif number==10:
        return "Equal"

    pass

def loop_sum(n):
    """
    Calculate sum of numbers from 1 to n using a loop.
    Args:
        n (int): Upper limit
    Returns:
        int: Sum of numbers
    """
    sum = 0
    for i in range(1,n+1):
        sum = sum+i 
    
    return sum

    pass

def list_operations(numbers):
    """
    Perform operations on a list of numbers.
    Args:
        numbers (list): List of numbers
    Returns:
        tuple: (sum, max, min)
    """

    sum=0
    max=numbers[0]
    min=numbers[0]

    for num in numbers:
        sum = sum+num
        if(max<num):
            max = num
        if(min>num):
            min=num

    my_tuple = (sum,max,min)
    return my_tuple
    pass


def dict_operations(students_dict):
    """
    Find students with scores above 80.
    Args:
        students_dict (dict): Dictionary of student names and scores
    Returns:
        list: Names of students with scores > 80
    """
    student_with_80=[]
    for key,value in students_dict.items():
        if(value > 80):
            student_with_80.append(key) 

    return student_with_80   

    pass

def set_operations(list1, list2):
    """
    Find common elements between two lists.
    Args:
        list1 (list): First list
        list2 (list): Second list
    Returns:
        set: Common elementsßß
    """
    common_data = set(set(list1) & set(list2))
    return common_data
    pass

def arithmetic_ops(a, b):
    """
    Perform arithmetic operations.
    Args:
        a (float): First number
        b (float): Second number
    Returns:
        dict: Results of arithmetic operations
    """
    dict_ops = {}
    dict_ops["sum"] = a+b
    dict_ops["difference"] =a-b
    dict_ops["product"] =a*b
    dict_ops["quotient"] =a/b

    return dict_ops
    
    pass

def logical_ops(x, y):
    """
    Perform logical operations.
    Args:
        x (bool): First boolean
        y (bool): Second boolean
    Returns:
        dict: Results of logical operations
    """

    dict_ops = {}
    dict_ops["and"] = x and y
    dict_ops["or"] = x or y
    dict_ops["not_x"] = not x

    return dict_ops

    pass

def bitwise_ops(a, b):
    """
    Perform bitwise operations.
    Args:
        a (int): First integer
        b (int): Second integer
    Returns:
        dict: Results of bitwise operations
    """

    dict_ops = {}
    dict_ops["and"] = a & b
    dict_ops["or"] = a | b
    dict_ops["xor"] = a ^ b

    return dict_ops
    pass