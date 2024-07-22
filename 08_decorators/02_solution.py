
def debug(func):
    print("inside debugg")
    def wrapper(*args, **kwargs):
         args_value = ', '.join(str(arg) for arg in args)
         list = []
         for arg in args:
            list.append(type(arg)) 
        #  print(f"stru : {list}")
         kwargs_value = ', '.join(f"{k}={v}" for k, v in kwargs.items() )
        #  print(f"calling: {func.__name__} with args {args_value} and kwargs {kwargs_value}")
         print("wrapper function inside")
        #  a = 1/0;
        #  print(a);
         return func(*args, **kwargs)
    return wrapper


# def hello():
#     print("Hello")

# @debug
def greet(name, n, greeting="Hello"):
    print("greet function inside")

# greet(2, "saad", greeting="hanji")

debug(greet)(2, "saad", greeting="hanji")
