import random
from math import sin, cos, pi, tan, sqrt

# Your job is to create better version of create_expression and
# run_expression to create random art.
# Your expression should have a __str__() function defined for it.


def create_expression():
    """This function takes no arguments and returns an expression that
    generates a number between -1.0 and 1.0, given
    return expr x and y coordinates."""

    a = random.triangular()
    z = random.random()
    m = z - 1
    n = z - 10
    o = a + z * pi
    gauss_graph = random.gauss(m, n)


    def function_one(x, y):

        return sin(sin(x) + cos(y) * pi * sin(a * o))

    def function_two(x, y):
        return sin((gauss_graph * sin(x) + sin(y)) * a)
    def function_three(x, y):
        return (sin(a + z) + (pi * x)) + o**2
    def function_four(x, y):
        triangle = random.triangular(x, y)
        return sin(sin(a * x) + tan(y)) + sin((sin(a * -x))) * ((x + triangle**2) - y)
    def function_five(x, y):
        triangle = random.triangular(z,m)**2
        return sin(triangle * -x * y) + pi**2
    def function_six(x, y):

        var = random.uniform(x,y) * (pi * x * y)/ 2

        return var
    def function_seven(x, y):
        return sin(x + y) + cos(y) * ((pi**2) / z)


    function_list = [function_one, function_two, function_three, function_four, function_five, function_six, \
                                                                                                function_seven]

    random_function = random.choice(function_list)

    def expr(x,y):


        return ((a * z * (random_function(x, y)) / pi) + (random_function(x, y) * a**2) + ((sin(random_function(x, y) \
                                                            + random_function(x, y)) * pi**2) * pi**2) * pi**2)




    return expr


def run_expression(expr, x, y):
    """This function takes an expression created by create_expression and
    an x and y value. It runs the expression, passing the x and y values
    to it and returns a value between -1.0 and 1.0."""
    return expr(x, y)
