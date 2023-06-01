print("#1__________________________________________")
def plus_one(number):
    return number + 1

add_one = plus_one
print(add_one(4))



print("#2__________________________________________")
def plus_one(number_):
    def add_one(number_):
        return number_ + 1


    result = add_one(number_)
    return result

print(plus_one(5))



print("#3__________________________________________")
def plus_one(Number_):
    return Number_ + 1

def function_call(function):
    number_to_add = 9
    return function(number_to_add)

print(function_call(plus_one))



#4 ______________________________________
def hello_function():
    def say_hi():
        return "Hi"
    return say_hi


hello = hello_function()
print(hello())



print("#5________________________________________")
def print_message(message):
    "Enclosong Function"
    def message_sender():
        "Nested Function"
        print(message)

    message_sender()

print_message("Some random message")



print("#6__________________________________________")
def uppercase_decorator(Function):
    def wrapper():
        func = Function()
        make_uppercase = func.upper()
        return make_uppercase

    return wrapper

def say_hi():
    return 'hello there'

decorate = uppercase_decorator(say_hi)
print(decorate())



print("#7____________________________________________")
def split_string(Function_):
    def wrapper_():
        funct = Function_()
        splitted_string = funct.split()
        return splitted_string

    return wrapper_

@split_string
@uppercase_decorator
def say_hi():
    return 'hello there'

print(say_hi())


print("#8______________________________________________")
def decorator_with_arguments(function_):
    def wrapper_accepting_arguments(arg1, arg2):
        print("My arguments are: {0}, {1}".format(arg1,arg2))
        function_(arg1, arg2)
    return wrapper_accepting_arguments


@decorator_with_arguments
def cities(city_one, city_two):
    print("Cities I love are {0} and {1}".format(city_one, city_two))

cities("Nairobi", "Accra")


print("#9______________________________________________")
def a_decorator_passing_arbitrary_arguments(function_to_decorate):
    def a_wrapper_accepting_arbitrary_arguments(*args,**kwargs):
        print('The positional arguments are', args)
        print('The keyword arguments are', kwargs)
        function_to_decorate(*args)
    return a_wrapper_accepting_arbitrary_arguments
#1_____
#@a_decorator_passing_arbitrary_arguments
#def function_with_no_argument():
#    print("No arguments here.")

#function_with_no_argument()
#2_____
# @a_decorator_passing_arbitrary_arguments
# def function_with_arguments(a, b, c):
#     print(a, b, c)

# function_with_arguments(1,2,3)

@a_decorator_passing_arbitrary_arguments
def function_with_keyword_arguments():
    print("This has shown keyword arguments")

function_with_keyword_arguments(first_name="Derrick", last_name="Mwiti")


print("#10___________________________________________________")
def decorator_maker_with_arguments(decorator_arg1, decorator_arg2, decorator_arg3):
    def decorator(func):
        def wrapper(function_arg1, function_arg2, function_arg3) :
            "This is the wrapper function"
            print("The wrapper can access all the variables\n"
                "\t- from the decorator maker: {0} {1} {2}\n"
                "\t- from the function call: {3} {4} {5}\n"
                "and pass them to the decorated function"
                .format(decorator_arg1, decorator_arg2,decorator_arg3,
                        function_arg1, function_arg2,function_arg3))
            return func(function_arg1, function_arg2,function_arg3)

        return wrapper

    return decorator

pandas = "Pandas"
@decorator_maker_with_arguments(pandas, "Numpy","Scikit-learn")
def decorated_function_with_arguments(function_arg1, function_arg2,function_arg3):
    print("This is the decorated function and it only knows about its arguments: {0}"
           " {1}" " {2}".format(function_arg1, function_arg2,function_arg3))

decorated_function_with_arguments(pandas, "Science", "Tools")