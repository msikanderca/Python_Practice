#ultil list for biggest number

def find_maxi(numbers):
    maxi = numbers[0]
    for number in numbers:
        if number >maxi:
            maxi = number
    return maxi


