from pathlib import Path

#Faz o apontamento do caminho de onde esta o arquivo e o carrega na memoria em uma variavel
path = Path('text_files/pi_digits.txt')
contents = path.read_text().rstrip()
#print(contents)

#leitura de linha por linha, e gera uma lista com cada linha

for line in contents.splitlines():
    print(line)
    print()
print(type(contents))
print(contents)


