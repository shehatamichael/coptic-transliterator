## Coptic Transliteration Tool

The vision of this project is to provide an easy, bulk transliteration service between Coptic and Latin script. The primary use case (Coptic --> Latin script) is to allow English speakers who do not read Coptic to follow along with church services by offering transliterated text with accurate and transparent pronunciations.

[![Downloads](https://pepy.tech/badge/coptictranslit)](https://pepy.tech/project/coptictranslit) [![PyPI version](https://badge.fury.io/py/coptictranslit.svg)](https://badge.fury.io/py/coptictranslit)

## Collaborators

* [Radobice Fass](mailto:radobice.fass@gmail.com)

## About the Transliterator

1) Accepts a single text file as input
2) Transforms a copy of the input file into Latin script using rule-based character mappings (implemented in Python)
3) Outputs the transformed copy of the input file (text file output format)"

## Pre-requisites to run this script

* Install [Miniconda](https://docs.conda.io/en/latest/miniconda.html)

* Once you have installed Miniconda, you will be able to install packages using the `conda` command. Run the following command to install the pynini package which is used in developing this tool

>```sh
>conda install -c conda-forge pynini
>```
 
## Installation

- This script is available through [PyPI](https://pypi.org/project/coptictranslit/)
>```sh
>pip install coptictranslit
>```

## Usage

* After successfull installation. Simply type this command in your shell/terminal after making the necessary changes and follow the prompt:
>```sh
>python3 -m translit.coptictranslit *insert your Coptic text file path here*
>```

## Pronunciation Guide

**TODO:** Update pronunciation guide when ready

## Release History
* 0.1.1
	* Updates to `README` and `LICENSE`
* 0.1.0
  * *Work in Progress* initial release

## References

**TODO:** Add all the references used

## License

`coptictranslit` is released under the MIT license. See `LICENSE.txt` for more information.

## Interested in Contributing?

Please contact Michael Shehata (shehatamichael4@gmail.com) and Radobice Fass (radobice.fass@gmail.com)
