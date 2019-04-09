def callback(a, b):
    print('Sum = {0}'.format(a+b))

def main(a,b,f=None):
    print('Add any two digits.')
    if f != None:
        f(a,b)


if __name__ == "__main__":
    main(1, 2, callback)