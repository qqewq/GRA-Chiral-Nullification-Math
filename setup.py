from setuptools import setup, find_packages

setup(
    name="gra_chiral_null",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "numpy",
        "scipy",
        "sympy",
        "matplotlib",
        "streamlit",
    ],
    author="GRA Collective",
    description="GRA chiral nullification: math of symmetry breaking",
    license="MIT",
)
