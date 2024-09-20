from pathlib import Path
#caso não exista, cria o arquivo
path = Path('text_files/programming.txt')
#escreve uma linha
#Só aceita string
path.write_text('I love programming')
#imprinmindo um arquivo com apenas uma linha
print('!!Imprinmindo o arquivo com apenas uma linha!!')
print(path.read_text())
print('-'*20)
#escreve multiplas linhas:
contents = "I love programming.\n"
contents += "I love creating new games.\n"
contents += "I also love working with data.\n"

path.write_text(contents)

#imprinmindo um arquivo com multiplas linha
print('!!Imprinmindo o arquivo com multiplas linha!!')
print(path.read_text())
print('-'*20)