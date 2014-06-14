How to build
--------------

```
python setuphello.py build_ext -i
```

Also you can use this command:

```
gcc -Wall -fPIC -c hello.c
gcc -shared -o hello.so hello.o
```

