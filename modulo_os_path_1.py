import os

print(os.getcwd())

if os.path.exists('diretorio_exemplo2'):
    print('existe')
else:
    print('não existe')
    
if os.path.exists('c:/windows/notepad.exe'):
    print('achei o notepad.exe')
    
else:
    print('não achei o notepad.exe')


#os.path.isfile -> verifica se um caminho é um arquivo ou pasta
c1 = 'c:/windows'
c2 = 'c:/windows/notepad.exe'
c3 = 'c:/blabla/notepad.exe/'

print(os.path.isfile(c1))#retorna false, pois c1 é nome da pasta
print(os.path.isfile(c2))#retorna true, pois c2 é nome de arquivo
print(os.path.isfile(c3))#retorna false, pois c3 não existe

caminho = 'c:/windows/system32/calc.exe'
#os.path.basename -> recebe um caminho como entrada e retorna o nome do arquivo como saída
print(os.path.basename(caminho))

#os.path.basename -> recebe um caminho como entrada e retorna o nome do diretório como saída
print(os.path.dirname(caminho))


#os.path.abspath - > concatena o dioretório corrente com o nome de um arquivo
print(os.path.abspath('blabla.txt'))

#os.path.split -> separa o caminho em 2 partes, numa tupla: diretório e o arquivo
print(os.path.split(caminho))

