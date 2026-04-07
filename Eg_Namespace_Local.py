#Python Namespace Program Example

def outer_function():
    num = 20

    def inner_function():
        num = 30
        print('num =', num)

    inner_function()
    print('num =', num)


num = 10
outer_function()
print('num =', num)