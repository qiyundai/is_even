def mod(a, b):
    return a - a // b * b

def is_even(num):
    if mod(num, 2) == 0:
        print("it's even!")
    else:
        print("No it ain't")

youtype = input("Enter a number: ")

is_even(int(youtype))