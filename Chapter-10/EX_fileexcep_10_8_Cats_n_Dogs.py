'''10-8. Cats and Dogs: Make two files, cats.txt and dogs.txt. Store at least three 
names of cats in the first file and three names of dogs in the second file. Write 
a program that tries to read these files and print the contents of the file to the 
screen. Wrap your code in a try-except block to catch the FileNotFound error, 
and print a friendly message if a file is missing. Move one of the files to a dif
ferent location on your system, and make sure the code in the except block 
executes properly.'''

from pathlib import Path

path_dog = Path('text_files/dogs.txt')
path_cat = Path('text_files/cats.txt')

try:
    dog_names=path_dog.read_text()
except FileNotFoundError:
    print(f'The file {path_dog} was not found int the path.')
else:
    print('!!DOG NAMES!!')
    print(dog_names)

try:
    cat_names=path_cat.read_text()
except FileNotFoundError:
    print(f'The file {path_cat} was not found int the path.')
else:
    print('!!CAT NAMES!!')
    print(cat_names)