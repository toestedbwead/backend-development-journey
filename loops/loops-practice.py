'''
In the print_numbers function, write a for-loop from scratch that logs the numbers 0-199 to the console.
'''
def print_numbers():
    for i in range(0,200):
        print(i)


# SHORTER version bc python assumes i = 0
def print_numbers():
    for i in range (200):
        print(i)

# Don't edit below this line


def test():
    print("Printing numbers from 0 to 199:")
    print_numbers()
    print("=====================================")


def main():
    test()


main()
