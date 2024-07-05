from setuptools import setup, find_packages

setup(
    name='minpy',
    version='0.1.0',
    packages=find_packages(where="src"),
    package_dir={'': 'src'},
    include_package_data=True,
    package_data={
        '': ['libminpy.so'],
    },
    install_requires=[

    ],
)
