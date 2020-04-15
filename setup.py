import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="coptic-translit-mshehata", # Replace with your own username
    version="0.1",
    author="Michael Shehata",
    author_email="shehatamichael4@gmail.com",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/shehatamichael/coptic-transliteration",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: GNU GPLv3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)