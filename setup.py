from setuptools import setup, find_packages

with open("requirements.txt", 'r') as f:
    reqs = f.readlines()

setup(
 name='Aminoacid',
 version='0.1',
 description='Game to learn and test the knowledge of aminoacids.',
 url='https://github.com/cbaruselli/aminoacid',
 author='cbaruselli',
 author_email='chloe.baruselli@epfl.ch',
 install_requires=reqs,
 license='MIT',
 packages=find_packages(),
 zip_safe=False
 )