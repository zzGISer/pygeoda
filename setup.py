#!/usr/bin/env python
import sys, os
import setuptools
from distutils.core import setup, Extension

OS_NAME = 'linux'

INCLUDE_DIRS = [
    './deps/include',
    './deps/libgeoda/include',
    './deps/lib/' + OS_NAME + '/wx/include/base-unicode-static-3.0'
]

LIBRARY_DIRS = ['/usr/lib']
LIBRARIES = [] # -lxxx

LIBRARY_DIRS += ['/usr/lib/x86_64-linux-gnu']
LIBRARIES = []

SWIG_OPTS = ['-c++']

EXTRA_COMPILE_ARGS = [
    '-std=c++11',
]


EXTRA_LINK_ARGS = []

EXTRA_OBJECTS = []

if OS_NAME == 'linux':
    EXTRA_OBJECTS = [
        './deps/lib/' + OS_NAME + '/libcurl.a',
        './deps/libgeoda/lib/' + OS_NAME + '/libgeoda.a',
        './deps/lib/' + OS_NAME + '/libboost_thread-mt.a',
        './deps/lib/' + OS_NAME + '/libboost_system-mt.a',
        './deps/lib/' + OS_NAME + '/libboost_chrono-mt.a',
        './deps/lib/' + OS_NAME + '/libboost_date_time-mt.a',
        './deps/lib/' + OS_NAME + '/libgdal.a',
        './deps/lib/' + OS_NAME + '/libgeos_c.a',
        './deps/lib/' + OS_NAME + '/libgeos.a',
        './deps/lib/' + OS_NAME + '/libproj.a',
        './deps/lib/' + OS_NAME + '/libwx_baseu-3.0.a',
        './deps/lib/' + OS_NAME + '/libwxregexu-3.0.a',
        './deps/lib/' + OS_NAME + '/libANN.a',
        './deps/lib/' + OS_NAME + '/libiconv.a',
    ]

SOURCE_FILES  = [
    'pygeoda/libgeoda.cpp'
]
 
extensions = [Extension('pygeoda._libgeoda',
                        sources=SOURCE_FILES,
                        include_dirs=INCLUDE_DIRS,
                        swig_opts=SWIG_OPTS,
                        extra_compile_args=EXTRA_COMPILE_ARGS,
                        extra_link_args=EXTRA_LINK_ARGS,
                        library_dirs=LIBRARY_DIRS,
                        runtime_library_dirs=LIBRARY_DIRS,
                        libraries=LIBRARIES,
                        extra_objects=EXTRA_OBJECTS),]

setup (name = 'pygeoda',
       version = '0.0.1',
       author = "Xun Li",
       author_email = "lixun910@gmail.com",
       url = "https://github.com/lixun910/libgeoda",
       description = """Python wrapper for GeoDa""",
       ext_modules = extensions,
       packages=['pygeoda']
      )

