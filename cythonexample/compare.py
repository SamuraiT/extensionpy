#! /usr/bin/env python
# coding: utf-8
"""
Copyright 2014 Tatsuro Yasukawa.

Distributed under the GNU General Public License at
gnu.org/licenses/gpl.html.
"""
import time
from fizzbuzz import fizzbuzz
from fizzbuzz2 import fizzbuzz as fz2

def runtime(f, t):
    s = time.time()
    f(t)
    return time.time() - s


def main(size=1000000):
    t = range(size)
    fz = runtime(fizzbuzz,t)
    fz2t = runtime(fz2, t)
    return fz, fz2t
if __name__ == '__main__':
    import sys
    print main()

