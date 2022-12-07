import math
class User:

    def __init__(self, username, password):
        self.messages = []
        self.n = None 
        self.e = None
        self.private_key = None
        self.username = username
        self.password = password


    # find e, the second part of the public key. If fails return -1
    def set_public_key(self, prime1, prime2):
        if self.n != None or self.e != None:
            return

        self.n = prime1 * prime2
        limit = (prime1 - 1) * (prime2 - 1)
        
        for i in range(2, limit):
            if math.gcd(i, limit) == 1:
                self.e = i
                break

        self.set_private_key(prime1, prime2)


    # sets the private key based on the randomly selected prime numbers
    def set_private_key(self, prime1, prime2):
        if self.private_key != None:
            return
        t = (prime1 - 1) * (prime2 - 1)
        
        i = 1
        while not (((t * i) + 1) / self.e).is_integer():
            i += 1

        self.private_key = int(((t * i) + 1) / self.e)
        

    # returns the two numbers that make up the public key
    def get_public_key(self):
        return [self.n, self.e]


    # takes a message, converts it to a list of ascii values, and then sends a list of encrypted characters
    def send_encrypted_message(self, message):
        # first, convert the message to ascii characters
        ascii_message = []
        for c in message:
            ascii_message.append(ord(c))

        encrypted_message = []
        for ascii in ascii_message:
            encrypted_message.append(ascii ** self.e % self.n)
        
        self.messages.append(encrypted_message)
        

    def decrypt_message(self, password):
        if password != self.password:
            return "incorrect password"
        if len(self.messages) == 0:
            return "no messages"

        message = self.messages.pop(0)
        print("Encrypted message is: " + str(message))
        plaintext_ascii = []

        for encrypted in message:
            plaintext_ascii.append(int(encrypted ** self.private_key % self.n))

        res = ""
        for character in plaintext_ascii:
            res = res + chr(character)

        return res


    # check if a user has a given username
    def has_username(self, username):
        return self.username == username


        







