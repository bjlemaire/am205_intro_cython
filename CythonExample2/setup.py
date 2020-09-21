from setuptools import setup
from Cython.Build import cythonize

setup(ext_modules = cythonize("speed_test_cy.pyx"))
