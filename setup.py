#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Copyright (c) 2011, Scott Burns
All rights reserved.
"""

import os
import redcap

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


if __name__ == '__main__':
    if os.path.exists('MANIFEST'):
        os.remove('MANIFEST')    
    
    setup(name='PyCap',
        maintainer='Scott Burns',
        maintainer_email='scott.s.burns@gmail.com',
        description="""PyCap: Python interface to REDCap""",
        license='BSD (3-clause)',
        url='http://github.com/VUIIS/PyCap',
        version=redcap.__version__,
        download_url='http://github.com/VUIIS/PyCap',
        long_description=open('README.md').read() + '\n\n',
        packages=['redcap'],
        platforms='any',
        classifiers=(
                'Development Status :: 4 - Beta',
                'Intended Audience :: Developers',
                'Intended Audience :: Science/Research',
                'License :: OSI Approved',
                'Topic :: Software Development',
                'Topic :: Scientific/Engineering',
                'Operating System :: Microsoft :: Windows',
                'Operating System :: POSIX',
                'Operating System :: Unix',
                'Operating System :: MacOS'
                'Programming Language :: Python',
                'Programming Language :: Python :: 2.7',)
        )
