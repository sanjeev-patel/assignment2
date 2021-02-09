Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 16:33:24) [MSC v.1928 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import random
>>> colors=['red','black','green']
>>> results=random. choices(colors, k=16)
>>> results1=random. choices(colors,weights=[6,6,4])
>>> print(results)
['black', 'black', 'red', 'black', 'black', 'black', 'black', 'green', 'black', 'black', 'green', 'black', 'black', 'red', 'black', 'black']
>>> print(results1)
['green']
>>> 