numbers = input("Enter series of numbers: \n").split(" ")


def secondLargest(numbers):
    numbers.sort()
    print(numbers)
    print(numbers[1])


secondLargest(numbers)
