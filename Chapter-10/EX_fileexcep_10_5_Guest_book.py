from pathlib import Path

guestnames=list()

while True:
    name=input("Digite o nome[0 para encerrar]: ")
    if name=='0':
        break
    guestnames.append(name)

#Recebe o nome e o escreve no arquivo
#print(guestnames)


path = Path('text_files/guest_book.txt')
content=''
for name in guestnames:
    content+=name
    content+='\n'

path.write_text(content)

#Lê e mostra o arquivo
print(path.read_text())


