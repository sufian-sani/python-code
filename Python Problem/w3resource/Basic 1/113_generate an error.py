while True:
    try:
        n=int(input('Enter Number: '))
        break
    except ValueError:
        print("\nThis is not a number. Try again...")