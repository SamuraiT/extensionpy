実行
------

build
```
python setup.py build_ext --inplace
```

e.g
```
>>>import hello as say
>>>say.hello()
hello cython
````

w/o setup, you can use:
```
import pyximport
pyximport.install()
import calc
..
..
calc.add(1,2)
3
```
参考
----
[cython document](http://omake.accense.com/static/doc-ja/cython/src/userguide/tutorial.html)
