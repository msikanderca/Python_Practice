def my_dec(f):
    def wrap():
        print ("Before function execution")
        f()
        print("After function execution")
    return wrap
@my_dec
def say_hello():
    print("Hello!")
say_hello()