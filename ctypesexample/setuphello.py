#! /usr/bin/env python
# coding: utf-8
"""
Copyright 2014 Tatsuro Yasukawa.

Distributed under the GNU General Public License at
gnu.org/licenses/gpl.html.
"""


from distutils.core import setup, Extension
module = Extension('hello', ['hello.c'])
setup(
      name='hello',
      version='1.0',
      ext_modules=[module],
)
