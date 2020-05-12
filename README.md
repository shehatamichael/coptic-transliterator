## Coptic Transliteration Tool

The vision of this project is to provide an easy, bulk transliteration service between Coptic and Latin script. The primary use case (Coptic --> Latin script) is to allow English speakers who do not read Coptic to follow along with church services by offering transliterated text with accurate and transparent pronunciations.

🚧 ***This script is a work-in-progress and updates will be made regularly to support more rules*** 🚧

## Disclaimer

This tool is still in development and we are working on expanding this as fast as we can. This tool supports 1-to-1 mapping for all Coptic letters. Special environement (1:Multiple mapping) is currently supported for the following letters:

Alpha -- ⲁ\
Veeta -- ⲃ\
Gamma -- ⲅ\
Ei -- ⲉ\
Eeta -- ⲏ

[![Downloads](https://pepy.tech/badge/coptictranslit)](https://pepy.tech/project/coptictranslit) [![PyPI version](https://badge.fury.io/py/coptictranslit.svg)](https://badge.fury.io/py/coptictranslit)

## Copyright and license

`coptictranslit` is released under the MIT license. See `LICENSE.txt` for more information.

## Citation

If you use this tool in your program or research, we would appreciate if you cite this paper:

> [Coptic Transliteration Tool](https://github.com/shehatamichael/coptic-transliterator/blob/master/Coptic%20Transliteration%20Tool.pdf), May 2020, Michael Shehata, Montclair State University of New Jersey, U.S.,.

## Collaborators

* Michael Shehata (shehatamichael4@gmail.com)
* Radobice Fass (radobice.fass@gmail.com)

## About the Transliterator

1) Accepts a single text file as input
2) Transforms a copy of the input file into Latin script using rule-based character mappings (implemented in Python)
3) Outputs the transformed copy of the input file (text file output format)

## Pre-requisites to run this script

* Install [Miniconda](https://docs.conda.io/en/latest/miniconda.html)

* Once you have installed Miniconda, you will be able to install packages using the `conda` command. Run the following command to install the Pynini package which is used in developing this tool

>```sh
>conda install -c conda-forge pynini
>```
 
🚨 **Note:** Having troubles installing Pynini? Try again after creating a new Conda environment:

>```sh
>conda create --name coptic
>conda update --all
>conda install --name coptic -c conda-forge pynini
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

## IPA Pronunciation Guide

"a" - [ɑː] as in "mark"\
"l" - [l] as in "lion"\
"r" - [r] as in "rope"\
"n"- [n] as in "no"\
"s" - [s] as in "see"\
"m" - [m] as in "may"\
"sh" - [ʃ] as in "she"\
"k" - [k] as in "key"\
"i" - [i] as in "eat"\
"e" - [ɛ] as in "send"\
"h" - [h] as in "happy"\
"t" - [t] as in "time"\
"ph" - [f] as in "Phil"\
"v" - [v] as in "vacation"\
"z" - [z] as in "zoo"\
"x" - [k s] as in "taxi"\
"o" - [oʊ] as in "code"\
"p" - [p] as in "pizza"\
"ps" - [p s] as in "wraps"\
"kk" - [k] as in "key"\
"mm" - [m] as in "may"\
"nn" - [n] as in "no"\
"ng" - [ŋ] as in "sing"\
"ia" - [i ə] as in "idea"\
"b" - [b] as in "boy"\
"g" - [g] as in "game"\
"d" - [d] as in "day"\
"th" - [θ] as in "thanks"\
"ch" - [tʃ] as in "chart"\
"w" - [w] as in "way"\
"dh" - [ð] as in "they"\
"gh" - [ɣ] as in "غني" (closest English equivalent is [g])\
"kh" - [x] as in "خمسة" (closest English equivalents are either [k] or [h])\
" ' " - [ʔ] as in "uh-oh" (sound just preceding "u" and "o", known as a glottal stop)"

## Release History
* 1.0
	* First official release
* 0.1.2
	* Updates to `README` and minor updates to script message prompt
* 0.1.1
	* Updates to `README` and `LICENSE`
* 0.1.0
  * *Work in Progress* initial release

## References

The rules have been mainly gathered from senior Coptic readers and experts in our Coptic churches.

* Makar, Father Kyrillos. The Coptic Language. Coptic Orthodox Diocese of the Southern USA. Retrieved from https://www.suscopts.org/deacons/coptic/FT-Coptic%20Language-Lectures.pdf.

* K. Gorman. 2016. Pynini: A Python library for weighted finite-state grammar compilation. In Proc. ACL Workshop on Statistical NLP and Weighted Automata, 75-80.


## Interested in Contributing?

Please contact Michael Shehata (shehatamichael4@gmail.com) and Radobice Fass (radobice.fass@gmail.com)
