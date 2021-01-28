def myFunc(arg1,arg2):
    """
    function documentation
    myFunc--->prints2 arguments
    Parameters:
    arg1:lorem ipsum
    arg2: lo
    """
    print(arg1,arg2)
def main():
    print(myFunc.__doc__)
if __name__=="__main__":
    main()
