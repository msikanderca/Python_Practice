def count(n):
    num =1
    while num <= n:
        yield num # this makes our function a generator
        num +=1
#using generator
for number in count(10):
    print(number)