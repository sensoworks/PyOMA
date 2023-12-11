from setuptools import setup, find_packages
import codecs
import os

def readme():
    with open('README.md') as f:
        README = f.read()
    return README

VERSION = "1.5"
DESCRIPTION = "PyOMA allows the experimental estimation of the modal parameters (natural frequencies, mode shapes, damping ratios) of a structure from measurements of the vibration response in operational condition."

# Setting up
setup(
    name="Py-OMA",
    version=VERSION,
    author="Dag Pasquale Pasca, Angelo Aloisio, Marco Martino Rosso, Stefanos Sotiropoulos",
    author_email="<supportPyOMA@polito.it>",
    license="GNU General Public License v3 (GPLv3)",
    description=DESCRIPTION,
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/dagghe/PyOMA",
    packages=find_packages(),
    install_requires=['numpy==1.24.3','scipy==1.10.1','pandas==2.0.2','matplotlib==3.7.1','seaborn==0.12.2','mplcursors==0.5.2'],
    keywords=['operational modal analysis', 'ambient vibration modal test', 'structural dynamics', 'frequency domain decomposition', 'stochastic subspace identification', 'structural health monitoring'],
    classifiers=[
        "Programming Language :: Python :: 3",
    ]
)
