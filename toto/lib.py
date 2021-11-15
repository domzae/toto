from termcolor import colored

def whats_my_name():

    return "Hello my name is Dom"

def who_am_i():

    name = whats_my_name()

    # difficult to test since the function returns None implicitly
    print(colored(name, "blue"))