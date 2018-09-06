# Error Handling
def inp(a):
    while True:
        try:
            n = int(input(a))
        except ValueError:
            print('Please enter a number only !!')
        else:
            return n

print(inp("Enter a number: "))



try:
    while x:
        print("Hello\n")
    raise NameError
except NameError as e:
    print(e)
finally:
    print("Done")