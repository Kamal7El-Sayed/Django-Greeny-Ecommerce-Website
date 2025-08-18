import random

def generate_code(lenght=8):
    numbers ='0123456789'
    code = ''.join(random.choice(numbers) for _ in range(lenght))
    return code