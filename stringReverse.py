#written in Python version 3.7.2

import string
import random

num_char = 10
num_int = 3

string = ''.join(random.choice(string.ascii_letters) for _ in range(num_char)) + ''.join(random.choice(string.digits) for _ in range(num_int))
reversedString = string[::-1]

f = open("Output.txt", "w");
f.write(string + "\n" + reversedString)
f.close()
