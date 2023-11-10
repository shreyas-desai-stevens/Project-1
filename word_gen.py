import random
def generate_random_word(length):
    characters = 'abcdefghijklmnopqrstuvwxyz'
    random_word = ''.join(random.choice(characters) for _ in range(length))
    return random_word

with open('test\\wc.test_4.in','w') as file:
    for i in range(1000):
        for j in range(1000):
            word = generate_random_word(j)
            file.write(f"{word}\n")