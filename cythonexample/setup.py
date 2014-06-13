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

hello_modules = [Extension("hello", ["hello.pyx"])]

setup(
    name = 'Hello cython module',
    cmdclass = {'build_ext': build_ext},
    ext_modules = hello_modules
)

