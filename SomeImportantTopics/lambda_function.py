#lambda function-
#a lambda function is a small anonymous function without a name. It is defined using the lambda keyword
# ambda functions are often used in situations where a small function is required for a short period of time.
# They are commonly used as arguments to higher-order functions, such as map, filter, and reduce

# Function to double the input
def double(x):
  return x * 2

# Lambda function to double the input
lambda x: x * 2

# Lambda function to calculate the product of two numbers
# lambda x, y: x * y
product = lambda x, y: print(f'{x} * {y} = {x * y}')
product(2,4)