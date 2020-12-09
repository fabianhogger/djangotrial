
"""
def get_prime_factors(value):
    if value oxi  monos:
        prime_list=[]
        prime=2
        if value/2 oxi akeraios pame:
            prime=prime+1
        for value/prime  akeraios:
            value=value/prime
            prime_list.append(prime)
            if value monos:
                return prime_list
            prime=prime+2


    return prime_list=value
"""
def is_prime(number):
    if number > 1:
        for i in range(2, number):
            if (number % i) == 0:
                return False
    return True
def get_prime_factors(value):
    if not is_prime(value):
        print("DEBUG")
        prime_list=[]
        prime=2
        while True:
            print("WHILE CLAUSE")
            if (value/prime).is_integer():
                print("is intiger ",(value/prime))
                value=int(value/prime)
                print("next value ",value)
                prime_list.append(prime)
                print("prime_list",prime_list)
                if is_prime(value):
                    prime_list.append(value)
                    return prime_list
                if prime==2:
                    prime=prime+1
                else:
                    prime=prime+2
                print("new prime ",prime)
            elif prime<value:
                print("ELIF")
                if prime==2:
                    prime=prime+1
                    print("prime got to 3")
                else:
                    prime=prime+2
                print("prime", prime)
            else:
                break
    else:
        return value


returned=get_prime_factors(147)
print("returned :", returned)
