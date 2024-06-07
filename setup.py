from setuptools import setup, Extension, find_packages
from setuptools.command.build_ext import build_ext
from shutil import copyfile
import os

# Function to locate the CMakeLists.txt and run cmake and make
def build_extension():
    build_temp = os.path.join(os.getcwd(), 'build')
    os.makedirs(build_temp, exist_ok=True)
    os.system(f'cmake -S src -B {build_temp}')
    os.system(f'cmake --build {build_temp}')
    copyfile(os.path.join(build_temp, 'libminpy.so'), 'minpy/libminpy.so')

class CMakeBuild(build_ext):
    def run(self):
        build_extension()
        super().run()

setup(
    name='minpy',
    version='0.1',
    author='jojobaseedoil',
    author_email='jojobaseedoil@gmail.com',
    description='A Python library for multistage interconnection network structures',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/jojobaseedoil/minpy',
    packages=find_packages(),
    ext_modules=[Extension('minpy', sources=[])],
    cmdclass={'build_ext': CMakeBuild},
    package_data={'': ['build/libminpy.so']},  # Referência para o arquivo libminpy.so
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    install_requires=[
        
    ],
)