def init():

    print("Choose a number")
    try:
        number = int(input())
    except:
        print('NaN')
        init()
    while collatz(number) != 1:
        number = collatz(number)
def collatz(number):
    if number % 2 == 0:
        print(number / 2)
        return number / 2
    elif number % 2 != 0:
        print(3 * number + 1)
        return 3 * number + 1
    
init()
