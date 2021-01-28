def myFunc(arg1,arg2):
    """
    function documentation
    myFunc--->prints2 arguments
    Parameters:
    arg1:lorem ipsum
    arg2: lo
    """
    print(arg1,arg2)
#define functions that can take variable length of arguments
def addition(*args):
    result = 0
    for arg in args:
        result+=arg
    return result
# Use lambdas as in-place functions

def CelsisusToFahrenheit(temp):
    return (temp * 9/5) + 32

def FahrenheitToCelsisus(temp):
    return (temp-32) * 5/9

def main():
    print(myFunc.__doc__)
    ctemps = [0, 12, 34, 100]
    ftemps = [32, 65, 100, 212]
    print(list(map(FahrenheitToCelsisus,ftemps)))
    print(list(map(CelsisusToFahrenheit,ctemps)))
    #do it as a lambda
    print(list(map(lambda t:((t-32)*5/9),ftemps)))
    print(list(map(lambda t:(t*9/5+32),ctemps)))

if __name__=="__main__":
    main()
