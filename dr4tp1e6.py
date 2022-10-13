import os


c1 = os.stat(input('digite o nome do arquivo: '))

print(c1.st_size, " bytes")