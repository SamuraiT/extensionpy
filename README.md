C言語によるpython拡張チュートリアル
---------------------
プログラムの実行速度はアルゴリズムに依存しますが，比較ソートのアルゴリズムのように
どうあがいても計算量が向上しないことがよくあります．（比較ソートの計算量は`nlogn`）
それでも実行速度を向上させたい場合は，オーバヘッドを減らす，
より速いハードウェアを使用する，速い言語を使うなどの処置しかありません．
しかしながら，オーバヘッドを減らすにも限界がありますし，
速いハードウェアを使うにはコストがかかります．
開発言語を変えるのは生産性の低下などの懸念があります．

ハードウェア等によらず実行速度を向上させる簡単な解決方法として，
一部を速い言語で置き換える方法があります．

ここでは，pythonからc言語で記述した関数等を利用する方法を簡単に紹介します．


cython
------
[Click here](cythonexample/)

c types example
-----
[Click here](ctypesexample/)

c extension example
------------
[Click here](cextexexample/)


参考
----
[pythonの高速化](http://d.hatena.ne.jp/gumilab/20101109/1289310291)
[c/c++ wrapper for python](http://www.quark.kj.yamagata-u.ac.jp/~hiroki/python/?id=19)
[CやC++によるPythonの拡張](http://docs.python.jp/2.7/extending/extending.html)
