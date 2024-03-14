from .constants import clArgumentsListofQuestions,sArgumentsErrorMssg

# XOR of two numbers
def question1(**kwargs):
    arguments = clArgumentsListofQuestions[2]
    if len(kwargs) != len(arguments):
        raise Exception(sArgumentsErrorMssg)

    return int(kwargs[arguments[0]]) ^ int(kwargs[arguments[1]])

# sum of n-1 numbers
def question2(**kwargs):
    arguments = clArgumentsListofQuestions[5]
    if len(kwargs) != len(arguments):
        raise Exception(sArgumentsErrorMssg)
    
    iParam1 = int(kwargs[arguments[0]])
    iOutput = (iParam1-1)*iParam1//2
    return iOutput

# a**2 + b**2
def question3(**kwargs):
    arguments = clArgumentsListofQuestions[2]
    if len(kwargs) != len(arguments):
        raise Exception(sArgumentsErrorMssg)

    return int(kwargs[arguments[0]])**2 + int(kwargs[arguments[1]])**2

# fibonacci = Medium
def question4(**kwargs):
    arguments = clArgumentsListofQuestions[3]
    if len(kwargs) != len(arguments):
        raise Exception(sArgumentsErrorMssg)
    
    if int(kwargs[arguments[0]]) == 0:
        return 0
    elif int(kwargs[arguments[0]]) == 1:
        return 1
    
    return question4(**{arguments[0]:int(kwargs[arguments[0]])-1}) + question4(**{arguments[0]:int(kwargs[arguments[0]])-2})

# question 5 in bharath questions - square = Hard
def question5(**kwargs):
    arguments = clArgumentsListofQuestions[4]
    if len(kwargs) != len(arguments):
        raise Exception(sArgumentsErrorMssg)
    iParam = int(kwargs[arguments[0]])
    iOuput = iParam**2 - (iParam-1)**2
    return iOuput

# decimal -> octa decimal
def question6(**kwargs):
    arguments = clArgumentsListofQuestions[5]
    if len(kwargs) != len(arguments):
        raise Exception(sArgumentsErrorMssg)
    
    octadecimal = oct(int(kwargs[arguments[0]]))
    return octadecimal

# digit sum = Easy
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

# sum of all the previous squares
def question8(**kwargs):
    arguments = clArgumentsListofQuestions[7]
    if len(kwargs) != len(arguments):
        raise Exception(sArgumentsErrorMssg)
    iParam = int(kwargs[arguments[0]])
    iOutput = (iParam)*(iParam+1)*(2*iParam+1)//6
    return iOutput

# set bits count
def question9(**kwargs):
    arguments = clArgumentsListofQuestions[11]
    if len(kwargs) != len(arguments):
        raise Exception(sArgumentsErrorMssg)
    
    count = 0
    number = int(kwargs[arguments[0]])
    while number:
        count += number & 1
        number >>= 1
    return number

# odd & even question
def question10(**kwargs):
    arguments = clArgumentsListofQuestions[9]
    if len(kwargs) != len(arguments):
        raise Exception(sArgumentsErrorMssg)
    
    a = int(kwargs[arguments[0]])
    if (a**2)&1:
        return a**2+1
    else:
        return a**2
    
# a*b-(a+b)
def question11(**kwargs):
    arguments = clArgumentsListofQuestions[10]
    if len(kwargs) != len(arguments):
        raise Exception(sArgumentsErrorMssg)
    
    return int(kwargs[arguments[0]])*int(kwargs[arguments[1]])-(int(kwargs[arguments[0]])+int(kwargs[arguments[1]]))

# # count set bits and add = Hard
# def question12(**kwargs):
#     arguments = clArgumentsListofQuestions[11]
#     if len(kwargs) != len(arguments):
#         raise Exception(sArgumentsErrorMssg)
    
#     count = 0
#     number = int(kwargs[arguments[0]])
#     while number:
#         count += number & 1
#         number >>= 1
#     return number

# # (+5,-2) pattern of the word = Hard
# def question13(**kwargs):
#     arguments = clArgumentsListofQuestions[12]
#     if len(kwargs) != len(arguments):
#         raise Exception(sArgumentsErrorMssg)
    
#     word = kwargs[arguments[0]]
#     output = ""
#     for i in range(0,len(word),2):
#         output += chr( ord(word[i]) + 5 )
#         if i < len(word):
#             output += chr( ord(word[i]) - 2 )
#     return output



# 1 XOR
# 2 input = n and sum from 1 to n-1
# 3 a^2 + b^2
# 4 fibanacci
# 5 n^2 - n-1^2
# 6 decimal -> octa decimal
# 7 digit sum
# 8 sum from 1^2 + 2^2 + 3^2 + .... + n^2
# 9 set bit count
# 10 odd even question
# 11 a*b-(a+b)
# 