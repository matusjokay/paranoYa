# PythonC paranoYa
This repository shows basic implementation of calling C library in Python script. This repository is part of paranoYa project. 

Used libraries: 
+ ctypes

## Tutorial

Firstly, you have to create **Shared Object** (*.so*) from *.c* file. This can be done by command of GCC compiler:

```cc -fPIC -shared -o file.so file.c```

We can then use created Share Object in Python: 

```python
from ctypes import *
so_file = '/path/file.so'
object = CDLL(so_file)
```

Variable object then acts as a python class.
