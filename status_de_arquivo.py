import os

status = os.stat('c:/windows/win.ini')
print(status)

print(type(status))

print(status[0])

print(status.st_size)