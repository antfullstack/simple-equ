#This is a setup file for cython. It is to be modified only when a new module is using cython in its workflow

from setuptools import setup, Extension

extensions = [
    Extension(
        "geometry.trigonometry",
        sources=["simple_equ/geometry/trigonometry.c"],
    )
]

setup(
    package_dir={"": "simple_equ"},
    ext_modules=extensions,
)