import random

import string

def generate_password():

    password=random.choices(string.ascii_letters+string.digits,k=8)

    return password

    