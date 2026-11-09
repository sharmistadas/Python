# 1. WAD that counts how many times main function is called

def count_calls(func):
    count = 0

    def wrapper(*args, **kwargs):
        nonlocal count
        count += 1
        print("Function called:", count, "times")
        return func(*args, **kwargs)

    return wrapper


@count_calls
def main():
    print("Welcome to Python Decorators")


main()
main()
main()


# 2. WAD that accepts the function and prints all positional arguments

def print_positional(func):

    def wrapper(*args):
        print("Positional Arguments:", args)
        return func(*args)

    return wrapper


@print_positional
def main(a, b, c):
    print("Main Function Executed")


main(10, 20, 30)


# 3. WAD to print all positional arguments before executing

def before_execution(func):

    def wrapper(*args):
        print("Arguments Before Execution:", args)
        return func(*args)

    return wrapper


@before_execution
def main(a, b):
    print("Sum:", a + b)


main(15, 25)


# 4. WAD that prints all keyword arguments after executing main function

def after_execution(func):

    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print("Keyword Arguments After Execution:", kwargs)
        return result

    return wrapper 


@after_execution
def main(name, age, city):
    print("Name:", name)
    print("Main Function Executed")


main(name="Arjun", age=23, city="Hyderabad")


# 5. WAD that calculates the sum of all numerical arguments
# passed to a function

def sum_arguments(func):

    def wrapper(*args, **kwargs):
        total = sum(x for x in args if isinstance(x, (int, float))
                    and not isinstance(x, bool))

        total += sum(x for x in kwargs.values()
                     if isinstance(x, (int, float))
                     and not isinstance(x, bool))

        print("Sum of Numerical Arguments:", total)
        return func(*args, **kwargs)

    return wrapper


@sum_arguments
def main(a, b, c):
    print("Main Function Executed")


main(10, 20, 30)


# 6. WAD that checks all arguments are positive numbers.
# If not positive, do not call the main function.

def check_positive(func):

    def wrapper(*args, **kwargs):
        values = args + tuple(kwargs.values())

        if all(isinstance(x, (int, float))
               and not isinstance(x, bool) and x > 0
               for x in values):
            return func(*args, **kwargs)
        else:
            print("Invalid Arguments! Enter Positive Numbers Only.")

    return wrapper


@check_positive
def main(a, b, c):
    print("All arguments are positive numbers.")
    print("Sum:", a + b + c)


main(10, 20, 30)
main(10, -5, 30)