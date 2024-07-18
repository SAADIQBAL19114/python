

def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(key , ":", value)





print_kwargs(name="ironman" ,power="lazer")
print_kwargs(name="ironman")
print_kwargs(name="ironman" ,power="lazer" ,enemy="thanos")