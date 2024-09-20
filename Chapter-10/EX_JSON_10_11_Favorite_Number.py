''' 10-11. Favorite Number: Write a program that prompts for the user’s favorite 
number. Use json.dumps() to store this number in a file. Write a separate pro
gram that reads in this value and prints the message “I know your favorite  
number! It’s _____.”'''

from pathlib import Path
import json

#saving the favorite number in a json file
def save_to_json(path,num):
    path.write_text(json.dumps(num))
    return path

#reading the json file
def read_json(path):
    content=path.read_text()
    num=json.loads(content)
    print(f'“I know your favorite number! It’s {num}')

path=Path('text_files/favorite_num.json')
num=input('Type your favorite number: ')
arquivo=save_to_json(path,num)
arquivo=arquivo
read_json(arquivo)


