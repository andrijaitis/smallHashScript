import hashlib

def guess_password(real):
    chars = string.ascii_lowercase + string.digits
    attempts = 0
    for password_length in range(1, 4):
        for guess in itertools.product(chars, repeat=password_length):
            attempts += 1
            guess = ''.join(guess)
            # if guess == real:
            if hashlib.sha256(guess.encode('ascii')).hexdigest() == real:
                return 'password is {}. found in {} guesses.'.format(guess, attempts)
            print(guess, attempts)

# print(guess_password('abc'))

print(guess_password('ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad'))