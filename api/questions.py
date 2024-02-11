from .constants import clArgumentsListofQuestions,sArgumentsErrorMssg

# addition of two numbers
def question1(**kwargs):
    arguments = clArgumentsListofQuestions[0]
    if len(kwargs) != len(arguments):
        raise Exception(sArgumentsErrorMssg)

    return int(kwargs[arguments[0]]) + int(kwargs[arguments[1]])

# multiplication of two numbers
def question2(**kwargs):
    arguments = clArgumentsListofQuestions[1]
    if len(kwargs) != len(arguments):
        raise Exception(sArgumentsErrorMssg)

    return int(kwargs[arguments[0]]) * int(kwargs[arguments[1]])

# xor of two numbers
def question3(**kwargs):
    arguments = clArgumentsListofQuestions[2]
    if len(kwargs) != len(arguments):
        raise Exception(sArgumentsErrorMssg)

    return int(kwargs[arguments[0]]) ^ int(kwargs[arguments[1]])

# fibonacci
def question4(**kwargs):
    arguments = clArgumentsListofQuestions[3]
    if len(kwargs) != len(arguments):
        raise Exception(sArgumentsErrorMssg)
    
    if int(kwargs[arguments[0]]) == 0:
        return 0
    elif int(kwargs[arguments[0]]) == 1:
        return 1
    
    return question4({arguments[0]:int(kwargs[arguments[0]])-1}) + question4({arguments[0]:int(kwargs[arguments[0]])-2})

# question 5 in bharath questions - square
def question5(**kwargs):
    arguments = clArgumentsListofQuestions[4]
    if len(kwargs) != len(arguments):
        raise Exception(sArgumentsErrorMssg)
    
    return int(kwargs[arguments[0]])**int(kwargs[arguments[1]])-int(kwargs[arguments[1]])**int(kwargs[arguments[0]])

# mod 5
def question6(**kwargs):
    arguments = clArgumentsListofQuestions[5]
    if len(kwargs) != len(arguments):
        raise Exception(sArgumentsErrorMssg)
    
    return int(kwargs[arguments[0]])%5

# digit sum
def question7(**kwargs):
    arguments = clArgumentsListofQuestions[6]
    if len(kwargs) != len(arguments):
        raise Exception(sArgumentsErrorMssg)
    
    output = 0
    a = int(kwargs[arguments[0]])
    while a > 0:
        output += a%10
        a //= 10
        
    return output

# square and previous square
def question8(**kwargs):
    arguments = clArgumentsListofQuestions[7]
    if len(kwargs) != len(arguments):
        raise Exception(sArgumentsErrorMssg)
    
    return int(kwargs(arguments[0]))**2 + (int(kwargs[arguments[0]])-1)**2

# ascii sum of difference
def question9(**kwargs):
    arguments = clArgumentsListofQuestions[8]
    if len(kwargs) != len(arguments):
        raise Exception(sArgumentsErrorMssg)
    
    word = kwargs[arguments[0]]
    sum = sum(ord(char) for char in word)
    values = [ord(char) for char in word]
    difference = max(values) - min(values)
    
    return sum, difference

# question 1 in bharath questions - odd_even
def question10(**kwargs):
    arguments = clArgumentsListofQuestions[9]
    if len(kwargs) != len(arguments):
        raise Exception(sArgumentsErrorMssg)
    
    a = int(kwargs[arguments[0]])
    if (a**2)&1:
        return a**2+1
    else:
        return a**2
    
# add_subtract fn
def question11(**kwargs):
    arguments = clArgumentsListofQuestions[10]
    if len(kwargs) != len(arguments):
        raise Exception(sArgumentsErrorMssg)
    
    return int(kwargs[arguments[0]])*int(kwargs[arguments[1]])-(int(kwargs[arguments[0]])+int(kwargs[arguments[1]]))