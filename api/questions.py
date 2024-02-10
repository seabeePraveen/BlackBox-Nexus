from .constants import clArgumentsListofQuestions

def question1(**kwargs):
    arguments = clArgumentsListofQuestions[0]
    if len(kwargs) != len(arguments):
        raise Exception("arguments are not matched got more or less number of arguments please check once again")

    return int(kwargs[arguments[0]]) + int(kwargs[arguments[1]])

def question2(**kwargs):
    arguments = clArgumentsListofQuestions[1]
    if len(kwargs) != len(arguments):
        raise Exception("arguments are not matched got more or less number of arguments please check once again")

    return int(kwargs[arguments[0]]) + int(kwargs[arguments[1]])