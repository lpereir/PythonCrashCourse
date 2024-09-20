'''10-9. Silent Cats and Dogs: Modify your except block in Exercise 10-7 to fail 
silently if either file is missing.'''

from pathlib import Path

path_dog = Path('dogs.txt')
path_cat = Path('text_files/cats.txt')

try:
    dog_names=path_dog.read_text()
except:
    pass
else:
    print('!!DOG NAMES!!')
    print(dog_names)

try:
    cat_names=path_cat.read_text()
except :
    pass
else:
    print('!!CAT NAMES!!')
    print(cat_names)