numbers = [1,2,3,4,5,6,7,8,9]
numbers1 = [1,2,3,4,5,6,7,8,9,9,78]

def sumFirstAndLast(numb):
    counter = 0
    for first in numbers:
        for last in numbers1:
            print(first,last)
            print(first + last)
            counter += 1
    return counter
print(sumFirstAndLast(numbers))