def fnAddTwoNumbers(*args):
    arguments = ['a','b']
    if len(args) != len(arguments):
        raise Exception("arguments are not matched got more or less number of arguments please check once again")
    variables = dict(zip(arguments, args))

    return int(variables['a']) + int(variables['b'])

def fnMultiplyTwoNumbers(*args):
    arguments = ['a','b']
    if len(args) != len(arguments):
        raise Exception("arguments are not matched got more or less number of arguments please check once again")
    variables = dict(zip(arguments, args))

    return int(variables['a']) * int(variables['b'])