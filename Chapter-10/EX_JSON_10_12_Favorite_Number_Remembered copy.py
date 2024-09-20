''' 10-12. Favorite Number Remembered: Combine the two programs you wrote in 
Exercise 10-11 into one file. If the number is already stored, report the favorite 
number to the user. If not, prompt for the user’s favorite number and store it in a 
file. Run the program twice to see that it works.'''

from pathlib import Path
import json


#saving the favorite number in a json file
def save_to_json(path,num):
    path.write_text(json.dumps(num))
    return path

#reading the json file
def read_json(path):
    num=json.loads(path.read_text())
    print(f'“I know your favorite number! It’s {num}"')

path = Path('text_files/favorite_num.json')

try:
    favorite_number=read_json(path)
except:
    favorite_number=input('Type your favorite number: ')
    read_json(save_to_json(path,favorite_number))