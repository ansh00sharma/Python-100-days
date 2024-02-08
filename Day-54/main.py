###   Introduction to Flask Framework and Python Decorators    ###


inputs = eval(input())

def logging_decorator(function):
  def wrapper_function(*args):
    print(function.__name__, "(",*args,")")
    print(function(*args))
  return wrapper_function
  

@logging_decorator
def a_function(a, b, c):
  return a * b * c

a_function(inputs[0], inputs[1], inputs[2])


# input : [1,2,3]
# output: a_function (1 2 3)
#         6
