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