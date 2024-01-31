from setuptools import setup
from Cython.Build import cythonize

setup(
    ext_modules = cythonize(os.path.join("darmonpoints", "a_cython_file.pyx"))
)
