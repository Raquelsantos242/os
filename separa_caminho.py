import os


p = os.path.abspath('c:/windows/win.ini') #gera caminho absoluto
t = os.path.split(p) #separa p em duas partes: diretório e arquivo

p0 = t[0] #nome do diretório
p1 = t[1] #nome do arquivo
lista_dir = [] #lista que receberá as partes do arquivo

while p1:
    lista_dir.append(p1)
    t = os.path.split(p0) #divide p0 em duas partes
    p0 = t[0] #nome do diretório
    p1 = t[1] #nome do arquivo
    
lista_dir.append(p0)
lista_dir.reverse()
print(lista_dir)