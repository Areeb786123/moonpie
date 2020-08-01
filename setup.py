import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="moonpie-legedith", # Replace with your own username
    version="0.0.1",
    author="legedith",
    author_email="jatindehmiwal@gmail.com",
    description="Because I dont't wanna use git anymore",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/legedith",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    scripts=['bin/moonpie'],
)