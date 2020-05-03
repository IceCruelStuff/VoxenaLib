import setuptools

with open('README.md') as f:
    long_desc = f.read()

setuptools.setup(
    name='VoxenaLib-Podrum',
    version='0.0.1',
    author='Nougator, MFDGaming',
    author_email='mc.podrum.team@gmail.com',
    long_description=long_desc,
    long_description_content_type="text/markdown",
    url="https://github.com/Podrum/VoxenaLib",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GPLv3 License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6'
)
