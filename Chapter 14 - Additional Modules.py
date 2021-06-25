import os


print(os.getcwd())

#os.mkdir('NewDir')

#os.makedirs('anotherDir\\newnewDir')

#print(os.listdir())

#os.rmdir('NewDir')
# os.removedirs('anotherDir\\newnewDir')

#print(os.listdir())

os.chdir('C:\\Users\khale\Documents\Python Project')

print(os.getcwd())
print(os.listdir())

os.chdir('Proj2')
print(os.listdir())
print(os.stat('proj2.py'))

from datetime import datetime

creation_Time =os.stat('proj2.py').st_ctime
print(creation_Time)
print(datetime.fromtimestamp(creation_Time))

os.chdir('C:\\Users\khale\Documents\Python Project')

for dirname, dirs, files in os.walk(os.getcwd()):
    print("Current directory {}".format(dirname))
    print("Directories inside {}".format(dirs))
    print("Files insides {}".format(files))

import random

value = random.random()
print(value)

value = random.uniform(1, 10)
print(value)

value = random.randint(1, 10)
print(value)

colors = ['red', 'black', 'blue', 'green', 'yellow', 'orange']
# rand_idx = random.randint(0,len(colors)-1)
# print(colors[rand_idx])
rand_color = random.choice(colors)
print(rand_color)

weighted_rand_color = random.choices(colors, weights=[1,2,1,4,1,1], k=5)
print(weighted_rand_color)

deck = range(1,53)

random_cards = random.sample(deck, k=10)

print(random_cards)


