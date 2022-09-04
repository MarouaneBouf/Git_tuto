# Is n divisible by x and y?
def is_divisible(n,x,y):
    return n % x == 0 and n % y == 0

def is_prime(n):
    return all(n%i for i in range(2,n))