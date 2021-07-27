# Lambda functions are also called anonymous functions
# Anonymous functions are functions with no name 
# Lambda functions are generally used as an argument to a higher-order function 
# higher-order function is a function that takes in other functions as arguments
# Lambda functions should be in one line, it wont support multiple lines
# Lambda functions are very usefull in filter and map functions

# Syntax
lambda arguments: expression

# Example for lambda function with zero args 
>>> print_hello = lambda: print("Hello World!!!") # definition
>>> print_hello() # calling lambda function
Hello World!!!
>>> 

# Example for lambda function with one arg
>>> square = lambda x: x*x 
>>> square(3) 
9
>>> 

# Map example for lambda function
>>> numbers = [1, 2, 3, 4, 5]
>>> num_squares = list(map(lambda num: num*num, numbers))
>>> num_squares
[1, 4, 9, 16, 25]
>>> 

# Filter example for lambda function
>>> numbers = [1, 2, 3, 4, 5]
>>> even_num = list(filter(lambda num: num%2==0, numbers))
>>> even_num
[2, 4]
>>> 
