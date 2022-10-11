import os


c1 = input('digite o nome do arquivo: ')

def funcao(c1):
    if os.path.exists(c1):
        if os.path.isfile(c1):
            return('é arquivo')
        if os.path.isdir(c1):
            return('é pasta')
    else:
        return('não existe')
    
print(funcao(c1))