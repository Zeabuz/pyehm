from setuptools import setup, find_packages
from setuptools_scm import get_version
from glob import glob

from pybind11.setup_helpers import Pybind11Extension, build_ext

with open('README.md') as f:
    long_description = f.read()


core_sources = sorted(glob("./src/core/*.cpp"))
net_sources = sorted(glob("./src/net/*.cpp"))
utils_sources = sorted(glob("./src/utils/*.cpp"))

version = get_version()

ext_module = Pybind11Extension(
    '_pyehm',
    sources=['src/module.cpp', 'src/Docstrings.cpp', *core_sources, *net_sources, *utils_sources],
    include_dirs=[r'./src', r'./include'],
    define_macros=[('VERSION_INFO',  version)]
)

setup(
    name='pyehm',
    author="Lyudmil Vladimirov",
    author_email="sglvladi@liverpool.ac.uk",
    maintainer="University of Liverpool",
    url='https://github.com/sglvladi/pyehm',
    description='Python Efficient Hypothesis Management (PyEHM)',
    long_description=long_description,
    long_description_content_type='text/markdown',
    project_urls={
        'Documentation': 'https://pyehm.rtfd.io/',
        'Source': 'https://github.com/sglvladi/pyehm',
        'Issue Tracker': 'https://github.com/sglvladi/pyehm/issues'
    },
    packages=find_packages(exclude=('docs', '*.tests')),
    install_requires=['numpy', 'networkx', 'stonesoup', 'setuptools>=42', 'pydot', 'matplotlib'],
    extras_require={
        'dev': ['pytest-flake8', 'pytest-cov', 'flake8', 'sphinx', 'sphinx_rtd_theme',
                'sphinx-gallery>=0.8']
    },
    entry_points={'stonesoup.plugins': 'pyehm = pyehm.plugins.stonesoup'},
    python_requires='>=3.9',
    use_scm_version=True,
    keywords=['python', 'pyehm', 'ehm'],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: Eclipse Public License 2.0 (EPL-2.0)",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering",
        "Programming Language :: Python :: 3 :: Only",
        "Operating System :: OS Independent",
    ],
    cmdclass={"build_ext": build_ext},
    ext_modules=[ext_module],
)
