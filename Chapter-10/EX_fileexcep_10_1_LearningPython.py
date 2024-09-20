from pathlib import Path

path = Path('text_files/learning_python.txt')
contents = path.read_text()
#print the content
print(contents)

#storing the lines in a list and then looping over each line
lines = contents.splitlines()
count=1
for line in lines:
    print(f'{count}ª line: {line}')
    count+=1