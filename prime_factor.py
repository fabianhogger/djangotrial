
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


    return value
"""
def is_prime(number):
    if number > 1:
        for i in range(2, number):
            if (number % i) == 0:
                return False
    return True
def get_prime_factors(value):
    prime_list=[]
    prime=2
    while (prime<value):
        if (value/prime).is_integer():
            value=int(value/prime)
            prime_list.append(prime)
            if is_prime(value):
                prime_list.append(value)
                return prime_list
            if prime==2:
                prime=prime+1
            else:
                prime=prime+2
            



returned=get_prime_factors(12)
print("returned :", returned)

def get_primef2(N):
    factors=list()
    divisor=2
    while(divisor<=N):
        if(N%divisor)==0:
            factors.append(divisor)
            N=N/divisor
        else:
            divisor+=1
    return factors
returned=get_primef2(12)
print("returned :", returned)
