from pathlib import Path

#Faz o apontamento do caminho de onde esta o arquivo e o carrega na memoria em uma variavel
#path = Path('text_files/pi_digits.txt')
path = Path('text_files/pi_million_digits.txt')
contents = path.read_text()
#print(contents)

#leitura de linha por linha, e gera uma lista com cada linha
lines=contents.splitlines()
pi_string=''
for line in lines:
    pi_string+=line.lstrip()

birthday=input('Enter you birthday, in the form mmddyy: ')
if birthday in pi_string:
    print('You birthday appears in the first million digits of pi!')
else:
    print('You birthday does not appears in the first million digits of pi!')


