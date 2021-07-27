import string
import random

ran = range(0, 10)
up_letter = random.choice(string.ascii_uppercase)
rng = random.sample(ran, k=8)
print('\t{}{}{}{}{}{}{}{}{}'. format(rng[0], rng[1], rng[2], rng[3], rng[4], rng[5], rng[6], rng[7], up_letter))
