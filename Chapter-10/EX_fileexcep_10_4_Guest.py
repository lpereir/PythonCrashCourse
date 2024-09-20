from pathlib import Path

path = Path('text_files/guest.txt')
#Recebe o nome e o escreve no arquivo
path.write_text(input('Type you Name: '))
#Lê e mostra o arquivo
print(path.read_text())


