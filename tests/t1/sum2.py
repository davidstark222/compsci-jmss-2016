# copy the code from sum1.py into this file, THEN:
# change your program so it keeps reading numbers until it gets a -1, then prints the sum of all numbers read

def getNumbers():
    numbers = input("Please enter any amount of numbers, seperated by spaces: ").split()
    return numbers

done = True
while done:
    try:
        numbers = getNumbers()
        addition = 0
        go = False

        for number in numbers:
            if number == '-1':
                go = True
                break
            else:
                addition += int(number)
        if go == False:
            print("You have not input -1")
        else:
            print(addition)
            done = False
    except ValueError:
        print("You have not input a valid number")
