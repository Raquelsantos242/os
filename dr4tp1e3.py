import os


if os.name == 'posix':
    print(st_gid())
else:
    print('você não está usando o linux')
    
print(os.getpid())

