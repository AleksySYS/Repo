import sys


def case_1():
    list_of_numbers = [1, 5, 8, 10, 21]
    print("Case_1 before")
    try:
        result = list_of_numbers[5]
    except IndexError as ie:
        print(f'Exception caught {ie.args}')
    except Exception as exp:
        print(f'Exception caught {exp.args}')
    print("Case_1 after")

    try:
        result = list_of_numbers[5]
    except (IndexError, Exception) as e:
        print(f'Exception caught {e.args}')

def case_2(name: str):
    if len(name) <= 0:
        raise ValueError('Sting is empty')
    print(f'Given name is: {name}')

def case_3(number: int, divisor: int) -> float:
    result = 0
    try:
        result = number / divisor
    except ZeroDivisionError as zde:
        print(f'Nie dziel przez zero')
        result = sys.float_info.max
        # result = float(sys.maxsize)
    return result


def case_4(dictionary: dict):
    key = "items"
    items: list = dictionary[key]
    # items: list = dictionary.get(key)
    for item in items:
        print(item)


def case_6():
    raise NotImplementedError("Solved future")

def case_7():
    fd = None
    try:
        fd = open('C:\\aaa.txt')
    except IOError as i:
        print(f'Exception caught {i.args}')
    finally:
        if fd:
            print("File descriptor closing")
            fd.close()

def case_7_v2():
    try:
        with open('C:\\aaa.txt') as fd: # context_manager
            print("File is open")
    except IOError as i:
        print(f'Exception caught {i.args}')