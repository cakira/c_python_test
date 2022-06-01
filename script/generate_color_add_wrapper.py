#!/bin/env python3

from cffi import FFI

ffibuilder = FFI()

ffibuilder.cdef('''
    void get_result(char *color_result);
''')

ffibuilder.set_source(
    'color_add_wrapper',  # name of the output C extension
    '''
    #include "color_add.h"
    ''',
    sources=['color_add.c'],  # includes pi.c as additional sources
    libraries=[])  # on Unix, link with the math library


if __name__ == '__main__':
    ffibuilder.compile(tmpdir='ccolor_add')
