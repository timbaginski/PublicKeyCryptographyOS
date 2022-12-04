import random
import math
from user import User


primes= []
users = []

# reads primes.txt to put primes into a list
def read_primes():
    f = open("primes.txt", "r")
    primes = f.read().split(", ")
    for i in range(len(primes)):
        primes[i] = int(primes[i])
    return primes


# randomly selects a prime number from the list of primes
def select_primes():
    prime1 = random.randint(0, len(primes)-1)
    prime2 = random.randint(0, len(primes)-1)

    return prime1, prime2


def create_user(username, prime1, prime2):
    user = User(username=username)
    user.set_public_key(prime1, prime2)
    users.append(user)


def message_user(username, message):
    temp = None
    for user in users:
        if user.has_username(username):
            temp = user 
            break

    if temp == None:
        return False 

    user.send_encrypted_message(message)
    return True


def main():

    










    






