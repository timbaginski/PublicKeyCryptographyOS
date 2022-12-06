import random
import math
from user import User

users = []

# reads primes.txt to put primes into a list
def read_primes():
    f = open("primes.txt", "r")
    primes = f.read().split(", ")
    for i in range(len(primes)):
        primes[i] = int(primes[i])
    
    f.close()
    return primes


# randomly selects a prime number from the list of primes
def select_primes(primes):
    prime1 = random.randint(0, len(primes)-1)
    prime2 = random.randint(0, len(primes)-1)

    return [primes[prime1], primes[prime2]]


def create_user(username, password, prime1, prime2):
    user = User(username=username, password=password)
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

    temp.send_encrypted_message(message)
    return True

# returns the command line arguments to print out for the user
def get_help_message():
    res = "usage: [options]\n"
    res += "  options:\n"
    res += "    -send message recipient\n" 
    res += "    -read username password\n"
    res += "    -add  username password\n"
    res += "    -q"
    return res


# main function
def main():
    # first we must store our primes in our primes global variable
    primes = read_primes()
    print(get_help_message())
    command = input()
    command = command.strip()
    command = command.split()

    while len(command) > 0 and command[0] != "-q":
        if len(command) == 3 and command[0] == "-send":
            message_user(command[2], command[1])

        elif len(command) == 3 and command[0] == "-read":
            temp = None
            for user in users:
                if user.has_username(command[1]):
                    temp = user
                    break
            
            if temp == None:
                print("User not found")
            
            print(temp.decrypt_message(command[2]))
        
        elif len(command) == 3 and command[0] == "-add":
            primes = select_primes(primes)
            create_user(command[1], command[2], primes[0], primes[1])
        
        else:
            print(get_help_message())
        
        command = input()
        command = command.strip()
        command = command.split()

if __name__ == "__main__":
    main()



    


    










    






