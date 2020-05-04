#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 4/14/2020

@author: michaelshehata
"""

from sys import argv
import pynini


#sigma

coptic_sigma = pynini.union("ⲁ", "Ⲁ", "ⲃ", "Ⲃ", "ⲅ", "Ⲅ", "ⲇ", "Ⲇ", "ⲉ", "Ⲉ", "ⲋ", "Ⲋ", "ⲍ", "Ⲍ", "ⲏ", "Ⲏ", 
                            "ⲑ", "Ⲑ", "ⲓ", "Ⲓ", "ⲕ", "Ⲕ", "ⲗ", "Ⲗ", "ⲙ", "Ⲙ", "ⲛ", "Ⲛ", "ⲝ", "Ⲝ", "ⲟ", "Ⲟ", 
                            "ⲡ", "Ⲡ", "ⲣ", "Ⲣ", "ⲥ", "Ⲥ", "ⲧ", "Ⲧ", "ⲩ", "Ⲩ", "ⲫ", "Ⲫ", "ⲭ", "Ⲭ", "ⲯ", "Ⲯ", 
                            "ⲱ", "Ⲱ", "ϣ", "Ϣ", "ϥ", "Ϥ", "ϧ", "Ϧ", "ϩ", "Ϩ", "ϫ", "Ϫ", "ϭ", "Ϭ", "ϯ", "Ϯ")

latin_sigma = pynini.union("a", "A", "b", "B", "c", "C", "d", "D", "e", "E", "f", "F", "g", "G", "h", "H", "i", 
                           "I", "j", "J", "k", "K", "l", "L", "m", "M", "n", "N", "o", "O", "p", "P", "q", "Q", 
                           "r", "R", "s", "S", "t", "T", "u", "U", "v", "V", "w", "W", "x", "X", "y", "Y", "z", 
                           "Z")

punct_whitespace_sigma = pynini.union(r"!", r'"', r"#", r"$", r"%", r"&", r"'", r"(", r")", r"*",
                                      r"+", r",", r"-", r".", r"/", r":", r"<", r"=", r">", r"?",
                                      r"@", r"\[", r"\\", r"\]", r"^", r"_", r"`", r"{", r"|",
                                      r"}", r"~", " ", "\t", "\n", "\r")

wb = "[WB]"

ipa_sigma = pynini.union("æ", "ə", "ɛ", "ɑː")

vowels = pynini.union("ⲁ", "Ⲁ", "ⲟ", "Ⲟ", "ⲱ", "Ⲱ", "ⲓ", "Ⲓ", "ⲏ", "Ⲏ", "ⲉ", "Ⲉ")

sigma = pynini.union(coptic_sigma, latin_sigma, punct_whitespace_sigma, vowels, ipa_sigma, wb)

sigma_star = pynini.closure(sigma)


#rules

insert_wb = pynini.transducer("", "[WB]")
# pynini.t("", "[WB]") + sigma_star + pynini.t("", "[WB]")
# Add WB when coptic letters are on the left and whitespace or punctuation are on the right
rule_addwb_1 = pynini.cdrewrite(insert_wb, coptic_sigma, punct_whitespace_sigma, sigma_star)
# Add WB when whitespace or punctuation are on the left and coptic letters are on the right
rule_addwb_2 = pynini.cdrewrite(insert_wb, punct_whitespace_sigma, coptic_sigma, sigma_star)

rule_removewb = pynini.cdrewrite(pynini.t("[WB]", ""), "", "", sigma_star)

#alpha

alphatoa_1 = pynini.transducer("ⲁ", "æ")
rule_1 = pynini.cdrewrite(alphatoa_1, "", "ⲥ[WB]", sigma_star)

alphatoa_2 = pynini.transducer("ⲁ", "ə")
rule_2 = pynini.cdrewrite(alphatoa_2, "", wb, sigma_star)

alphatoa_3 = pynini.transducer("ⲁ", "ɛ")
###rule_3###

alphatoa_4 = pynini.transducer("ⲁ", "ɑː")
rule_4 = pynini.cdrewrite(alphatoa_4, "", "", sigma_star)


#veeta

veetatov = pynini.transducer("ⲃ", "v")
veetatob = pynini.transducer("ⲃ", "b")
#this rule should be executed first due to the overlap in the vowel "ⲓ"
rule_5 = pynini.cdrewrite(veetatob, "", "ⲓⲙ[WB]", sigma_star)
rule_6 = pynini.cdrewrite(veetatov, "", "ⲧ[WB]", sigma_star)
rule_7 = pynini.cdrewrite(veetatov, "", vowels, sigma_star)

rule_8 = pynini.cdrewrite(veetatob, "", "ⲣ", sigma_star)
rule_9 = pynini.cdrewrite(veetatob, "", "ⲥ", sigma_star)
rule_10 = pynini.cdrewrite(veetatob, "", wb, sigma_star)

#Gamma

gammaton = pynini.transducer("ⲅ", "n")
#this rule should be executed first
rule_11 = pynini.cdrewrite(gammaton, "", "ⲅ", sigma_star)

gammatog = pynini.transducer("ⲅ", "g")
rule_12 = pynini.cdrewrite(gammatog, "", "ⲓ", sigma_star)
rule_13 = pynini.cdrewrite(gammatog, "", "ⲉ", sigma_star)

gammatogh = pynini.transducer("ⲅ", "gh")
rule_14 = pynini.cdrewrite(gammatogh, "", "", sigma_star)

#delta

deltatoth = pynini.transducer("ⲇ", "th")
###rule_15###

deltatod = pynini.transducer("ⲇ", "d")
###rule_16###

# sooto6 = pynini.transducer("ⲋ", "6")
# rule_17 = pynini.cdrewrite(sooto6, "", sigma_star)

#eeta
eetatoy = pynini.transducer("ⲏ", "y")
#should be executed before ei
rule_18 = pynini.cdrewrite(eetatoy, "ⲉ", "", sigma_star)

#ei
eitoe_1 = pynini.transducer("ⲉ", "eɪ")
rule_19 = pynini.cdrewrite(eitoe_1, "", "ⲟ", sigma_star)

eitoe_2 = pynini.transducer("ⲉ", "e")
rule_20 = pynini.cdrewrite(eitoe_2, "", "", sigma_star)

eetatoee = pynini.transducer("ⲏ", "ee")
rule_21 = pynini.cdrewrite(eetatoee, "", "", sigma_star)

#1:1 mapping

onetoone_1 = pynini.transducer("ⲁ", "a")
rule_onetoone_1 = pynini.cdrewrite(onetoone_1, "", "", sigma_star)

onetoone_2 = pynini.transducer("ⲗ", "l")
rule_onetoone_2 = pynini.cdrewrite(onetoone_2, "", "", sigma_star)

onetoone_3 = pynini.transducer("ⲣ", "r")
rule_onetoone_3 = pynini.cdrewrite(onetoone_3, "", "", sigma_star)

onetoone_4 = pynini.transducer("ⲛ", "n")
rule_onetoone_4 = pynini.cdrewrite(onetoone_4, "", "", sigma_star)

onetoone_5 = pynini.transducer("ⲥ", "s")
rule_onetoone_5 = pynini.cdrewrite(onetoone_5, "", "", sigma_star)

onetoone_6 = pynini.transducer("ⲙ", "m")
rule_onetoone_6 = pynini.cdrewrite(onetoone_6, "", "", sigma_star)

onetoone_7 = pynini.transducer("ϣ", "sh")
rule_onetoone_7 = pynini.cdrewrite(onetoone_7, "", "", sigma_star)

onetoone_8 = pynini.transducer("ⲕ", "k")
rule_onetoone_8 = pynini.cdrewrite(onetoone_8, "", "", sigma_star)

onetoone_9 = pynini.transducer("ⲓ", "i")
rule_onetoone_9 = pynini.cdrewrite(onetoone_9, "", "", sigma_star)

onetoone_10 = pynini.transducer("ⲉ", "e")
rule_onetoone_10 = pynini.cdrewrite(onetoone_10, "", "", sigma_star)

onetoone_11 = pynini.transducer("ⲏ", "i")
rule_onetoone_11 = pynini.cdrewrite(onetoone_11, "", "", sigma_star)

onetoone_12 = pynini.transducer("ϩ", "h")
rule_onetoone_12 = pynini.cdrewrite(onetoone_12, "", "", sigma_star)

onetoone_13 = pynini.transducer("ⲧ", "t")
rule_onetoone_13 = pynini.cdrewrite(onetoone_13, "", "", sigma_star)

onetoone_14 = pynini.transducer("ϯ", "ti")
rule_onetoone_14 = pynini.cdrewrite(onetoone_14, "", "", sigma_star)

onetoone_15 = pynini.transducer("ϧ", "kh")
rule_onetoone_15 = pynini.cdrewrite(onetoone_15, "", "", sigma_star)

onetoone_16 = pynini.transducer("ⲫ", "ph")
rule_onetoone_16 = pynini.cdrewrite(onetoone_16, "", "", sigma_star)

onetoone_17 = pynini.transducer("ϥ", "f")
rule_onetoone_17 = pynini.cdrewrite(onetoone_17, "", "", sigma_star)

onetoone_18 = pynini.transducer("ⲍ", "z")
rule_onetoone_18 = pynini.cdrewrite(onetoone_18, "", "", sigma_star)

onetoone_19 = pynini.transducer("ⲝ", "x")
rule_onetoone_19 = pynini.cdrewrite(onetoone_19, "", "", sigma_star)

onetoone_20 = pynini.transducer("ⲱ", "o")
rule_onetoone_20 = pynini.cdrewrite(onetoone_20, "", "", sigma_star)

onetoone_21 = pynini.transducer("ⲡ", "p")
rule_onetoone_21 = pynini.cdrewrite(onetoone_21, "", "", sigma_star)

onetoone_22 = pynini.transducer("ⲯ", "ps")
rule_onetoone_22 = pynini.cdrewrite(onetoone_22, "", "", sigma_star)

onetoone_23 = pynini.transducer("ⲕⲕ", "kk")
rule_onetoone_23 = pynini.cdrewrite(onetoone_23, "", "", sigma_star)

onetoone_24 = pynini.transducer("ⲙⲙ", "mm")
rule_onetoone_24 = pynini.cdrewrite(onetoone_24, "", "", sigma_star)

onetoone_25 = pynini.transducer("ⲛⲛ", "nn")
rule_onetoone_25 = pynini.cdrewrite(onetoone_25, "", "", sigma_star)

onetoone_26 = pynini.transducer("ⲟⲓⲁ", "ia")
rule_onetoone_26 = pynini.cdrewrite(onetoone_26, "", "", sigma_star)

onetoone_27 = pynini.transducer("ⲟⲩⲱ", "o'o")
rule_onetoone_27 = pynini.cdrewrite(onetoone_27, "", "", sigma_star)

onetoone_28 = pynini.transducer("ⲃ", "b")
rule_onetoone_28 = pynini.cdrewrite(onetoone_28, "", "", sigma_star)

onetoone_29 = pynini.transducer("ⲅ", "g")
rule_onetoone_29 = pynini.cdrewrite(onetoone_29, "", "", sigma_star)

onetoone_30 = pynini.transducer("ⲇ", "d")
rule_onetoone_30 = pynini.cdrewrite(onetoone_30, "", "", sigma_star)

onetoone_31 = pynini.transducer("ⲑ", "th")
rule_onetoone_31 = pynini.cdrewrite(onetoone_31, "", "", sigma_star)

onetoone_32 = pynini.transducer("ⲟ", "o")
rule_onetoone_32 = pynini.cdrewrite(onetoone_32, "", "", sigma_star)

onetoone_33 = pynini.transducer("ⲩ", "u")
rule_onetoone_33 = pynini.cdrewrite(onetoone_33, "", "", sigma_star)

onetoone_34 = pynini.transducer("ⲭ", "ch")
rule_onetoone_34 = pynini.cdrewrite(onetoone_34, "", "", sigma_star)

onetoone_35 = pynini.transducer("ϭ", "ky")
rule_onetoone_35 = pynini.cdrewrite(onetoone_35, "", "", sigma_star)

#cdrewrite

cascade = pynini.optimize(rule_addwb_1@rule_addwb_2@rule_1@rule_2@rule_4@rule_5@
                          rule_6@rule_7@rule_8@rule_9@rule_10@rule_11@rule_12@
                          rule_13@rule_14@rule_18@rule_19@rule_20@rule_21@
                          rule_onetoone_1@rule_onetoone_2@rule_onetoone_3@
                          rule_onetoone_4@rule_onetoone_5@rule_onetoone_6@
                          rule_onetoone_7@rule_onetoone_8@rule_onetoone_9@
                          rule_onetoone_10@rule_onetoone_11@rule_onetoone_12@
                          rule_onetoone_13@rule_onetoone_14@rule_onetoone_15@
                          rule_onetoone_16@rule_onetoone_17@rule_onetoone_18@
                          rule_onetoone_19@rule_onetoone_20@rule_onetoone_21@
                          rule_onetoone_22@rule_onetoone_23@rule_onetoone_24@
                          rule_onetoone_25@rule_onetoone_26@rule_onetoone_27@
                          rule_onetoone_28@rule_onetoone_29@rule_onetoone_30@
                          rule_onetoone_31@rule_onetoone_32@rule_onetoone_33@
                          rule_onetoone_34@rule_onetoone_34@rule_removewb)


def translit(text):
    text = text.lower()
    text = (text @ cascade)
    return text.string()

script, filename = argv


def convert(filename):
	with open (filename, "r") as myfile:
		data=myfile.read()
		return data

script, file = argv

file = convert(file)

print("\n--------------------------------------------------")
print("Original text:\n")
print(file)


translit_string = translit(file)

print("\n--------------------------------------------------")
print("Transliterated text:\n")
print(''.join(translit_string))


print("\n--------------------------------------------------")
print("Would you like to save the transliterated text as a new file?")
print("(This will create a new file or overwrite if a file already exists.)")
save = input("> ")
if save == "yes" or save == "y" or save == "Yes" or save == "Y":
	print("What would you like to name the new file?")
	name = input("> ")
	txt = open(name, "w")
	txt.write(translit_string)
	print("File saved.")
else:
	print("File not saved.")