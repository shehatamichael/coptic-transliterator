from setuptools import Extension, setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

coptictranslittest = Extension(
    name="coptictranslittest",
    language="python",
    sources=[
        "src/coptic_translit.py",
        "src/file_to_string.py",
        "src/transliteratory.py",
    ],
)
setup(
    name="coptictranslittest",
    version="0.0.1",
    author="Michael Shehata",
    author_email="shehatamichael4@gmail.com",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/shehatamichael/coptic-transliteration",
    packages=find_packages(),
    install_requires=['pynini'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
