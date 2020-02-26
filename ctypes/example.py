from ctypes import *
so_file = '/home/mohan/paranoYa/c/lib.so'
example = CDLL(so_file)

print(example.cubicRes())