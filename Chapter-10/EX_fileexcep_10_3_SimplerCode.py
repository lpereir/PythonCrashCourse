from pathlib import Path

path = Path('text_files/learning_python.txt')
contents = path.read_text()
#print the content
print(contents)

#storing the lines in a list and then looping over each line
#replacing
lines = contents
count=1
for line in lines.splitlines():
    print(line.replace('Python','C'))
    count+=1

