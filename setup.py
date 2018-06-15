from setuptools import find_packages
from distutils.core import setup

packages = find_packages('src', exclude='src')
package_dir = {k: 'src/' + k.replace('.', '/') for k in packages}

setup(
    name='tec',
    version='2.0.7',
    description='Repositorio del curso de IA',
    url='https://...',
    author='Fabio Mora - Sergio Moya - Gabriel Venegas',
    author_email="g...@g....com",
    packages=packages,
    package_dir=package_dir
)
