# write a program that reads in 10 numbers, then prints the sum of those

def getNumbers():
    numbers = input("Please enter 10 numbers, seperated by spaces: ").split()
    while len(numbers) != 10:
        print("You must enter 10 numbers. Check to make sure they are seperated by spaces.")
        numbers = input("Please enter 10 numbers, seperated by spaces: ").split()
    return numbers

done = True
while done:
    try:
        addition = 0
        for number in getNumbers():
            addition += int(number)
        print(addition)
        done = False
    except ValueError:
        print("You have not input a valid number")