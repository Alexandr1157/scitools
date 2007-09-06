#!/usr/bin/env python
"""
Install scitools with easyviz

Usage:

python setup.py install [, --prefix=$PREFIX]
"""

import os, sys, socket, re, glob

try:
    import scitools
except ImportError:
    from os.path import abspath, join, dirname
    path = abspath(join(dirname(__file__), "lib"))
    sys.path.append(path)
    import scitools
    
if  __file__ == 'setupegg.py':
    # http://peak.telecommunity.com/DevCenter/setuptools
    from setuptools import setup, Extension
else:
    from distutils.core import setup

setup(
    version = str(scitools.version), 
    author = ', '.join(scitools.author),
    author_email = "<hpl@simula.no>",
    description = scitools.__doc__,
    license = "LGPL",
    name = "SciTools",
    url = "",
    package_dir = {'': 'lib'},
    packages = ["scitools",
                os.path.join("scitools", "easyviz"), 
		os.path.join("scitools", "pyPDE"),
		],
    package_data={'': ['scitools.cfg']},
    scripts = [os.path.join('bin', f) \
               for f in os.listdir('bin') if not (f.startswith('.') or f.endswith('~') or f.endswith('.old') or f.endswith('.bak'))],
	       )
	    
	       
               

    
