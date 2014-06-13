#! /usr/bin/env python
# coding: utf-8
"""
Copyright 2014 Tatsuro Yasukawa.

Distributed under the GNU General Public License at
gnu.org/licenses/gpl.html.
"""
import ctypes

def main():
    say = ctypes.CDLL('./hello.so')
    say.hello()

if __name__ == '__main__':
    main()

