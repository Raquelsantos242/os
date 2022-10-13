import os

executavel_com_path = os.environ['SYSTEMROOT'] + '\\System32\\calc.exe'
#print(executavel_com_path)

#os.spawnl(os.P_NOWAIT, executavel_com_path, ' ')

#os.startfile(executavel_com_path)
os.system(executavel_com_path)
