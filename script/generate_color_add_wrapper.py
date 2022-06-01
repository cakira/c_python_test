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

ffibuilder.embedding_api('''
    void get_color_a(char *);
    void get_color_b(char *);
''')

ffibuilder.embedding_init_code('''
    from color_add_wrapper import ffi
    from environment import environment

    @ffi.def_extern()
    def get_color_a(result):
        color = environment.get_color_a()
        for i in range(len(color)):
            result[i] = color[i].encode()
        result[len(color)] = b'\\x00'

    @ffi.def_extern()
    def get_color_b(result):
        color = environment.get_color_b()
        for i in range(len(color)):
            result[i] = color[i].encode()
        result[len(color)] = b'\\x00'
''')

if __name__ == '__main__':
    ffibuilder.compile(tmpdir='ccolor_add')
