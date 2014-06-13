#! /usr/bin/env python
# coding: utf-8
"""
Copyright 2014 Tatsuro Yasukawa.

Distributed under the GNU General Public License at
gnu.org/licenses/gpl.html.
"""


from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext


setup(
    name = 'c type example module',
    cmdclass = {'build_ext': build_ext},
    ext_modules = [Extension("fizzbuzz", ["fizzbuzz.pyx"])]

)
