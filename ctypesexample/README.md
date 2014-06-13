実行
----

```
gcc -Wall -fPIC -c hello.c -I/usr/include/python2.7
gcc -shared -o hello.so hello.o
```
