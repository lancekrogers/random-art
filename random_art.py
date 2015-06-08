import random
from math import sin, cos, sqrt, pi, tan

# Your job is to create better version of create_expression and
# run_expression to create random art.
# Your expression should have a __str__() function defined for it.


def create_expression():
    """This function takes no arguments and returns an expression that
    generates a number between -1.0 and 1.0, given
    return expr x and y coordinates."""
    mu = (3 + 9) / 2
    sd =  2.1
    gauss_graph = random.gauss(mu, sd)
    a = random.triangular()
    z = random.random()
    m = z + 1
    n = z + 10
    o = a + z * pi

    def function_one(x, y):

        return sin(sin(x) + cos(y) * pi * sin(a * o))

    def function_two(x, y):
        return sin((gauss_graph * sin(m) + sin(n)) * a) * pi
    def function_three(x, y):
        return (sin(a + z) + (pi * x)) + o
    def function_four(x, y):
        return sin(a * x) + tan(y)
    def function_five(x, y):
        num_list = [45, 67, 78, 3, 54, 8, 12]
        for num in num_list:
            five_value = (pi / num)
            return five_value
        return cos(five_value)

    function_list = [function_one, function_two, function_three, function_four, function_five]

    random_function = random.choice(function_list)

    def expr(x,y):
        num_list = [45, 67, 78, 3, 54, 8, 12]
        for num in num_list:
            five_value = (pi / num)


        return (random_function(x, y) * five_value)


    return expr


def run_expression(expr, x, y):
    """This function takes an expression created by create_expression and
    an x and y value. It runs the expression, passing the x and y values
    to it and returns a value between -1.0 and 1.0."""
    return expr(x, y)
