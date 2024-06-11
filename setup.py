from setuptools import Extension, setup

setup(
    ext_modules=[
        Extension(
            name="minpy",  # as it would be imported
                           # may include packages/namespaces separated by `.`

            sources=["src/Multistage.cpp", "src/Slider.cpp", "src/Omega.cpp"], # all sources are compiled into a single binary file
        ),
    ]
)