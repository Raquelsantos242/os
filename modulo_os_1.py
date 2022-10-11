import os

#obtém o nome do sistema operacional
#'posix', (linux, mac), 'nt', (windows), 'java'.
print(os.name)

#INFORMAÇÕES DE SISTEMA

#obter o usuário corrent -> getlogin()
print(os.getlogin())

#obter as variáveis de ambiente -> os.environ
print(os.environ)

#for k, v in os.environ.items(): print(k,v)

print(os.environ['HOMEDRIVE'])
print(os.environ['HOMEPATH'])

#obter o diretório corrente -> os.getcwd()
print(os.getcwd())

#obter o pid do seu ambiente Python -> os.pid()
print(os.getpid())

#INFMORMAÇÕES DE ARQUIVOS E DIRETÓRIOS

#Obter o diretório corrente -> os.getcwd()
print(os.getcwd())

#criar uma pasta dentro do diretório corrente -> os.mkdir()
#os.mkdir("diretorio_exemplo")

#renomear diretório -> os.rename()
os.rename("diretorio_exemplo", "diretorio_exemplo2")

#listar o conteúdo do diretório
#print(os.listdir('c:/Users/'))

print(os.listdir())

#mudar de diretório -> os.chrdir()
os.chrdir('..')
print(os.listdir())