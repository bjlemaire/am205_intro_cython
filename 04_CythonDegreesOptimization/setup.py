from setuptools import setup
from Cython.Build import cythonize

setup(ext_modules = cythonize(["compute_cy1.pyx",
                               "compute_cy2.pyx",
                               "compute_cy3.pyx"]))
