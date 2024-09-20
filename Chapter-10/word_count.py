from pathlib import Path

def count_words(path):
    '''Count the approximate number of words in a file.'''
    try:
        contents=path.read_text(encoding='utf-8')
    except FileNotFoundError:
        print(f'O arquivo {path} não existe')
    else:
        #Count the approximate number of words in the file:
        words=contents.split()
        num_words=len(words)
        print(f'!!The file {path} has about {num_words} words!!')


#path = Path('text_files/alice.txt')
#count_words(path)

filenames=['text_files/alice.txt','text_files/siddhartha.txt','text_files/moby_dick.txt','text_files/little_women.txt']
for filename in filenames:
    path = Path(filename)
    count_words(path)
