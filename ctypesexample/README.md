Build
----

```
gcc -Wall -fPIC -c hello.c -I/usr/include/python2.7
gcc -shared -o hello.so hello.o
```

or

```
python setuphello.py setup build_ext -i
```
