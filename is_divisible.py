
# main function
def main():
    number = 7
    print(is_prime(number))

# Is n divisible by x and y?
def is_divisible(n,x,y):
    return n % x == 0 and n % y == 0

#Check if prime
def is_prime(n):
    """
    Return True if all the numbers from 2 to n-1 are not divisors of n.
    
    :param n: the number to check
    :return: True or False
    """
    return all(n%i for i in range(2,n//2))
