#! /usr/bin/python3

from math import sqrt

print ('Tämä ohjelma askee HYPOTENUUSAN kahden sivun avulla')

kateetti1 = int(input('Anna 1. sivu : '))
kateetti2 = int(input('Anna 2. sivu : '))

hypotenuusa = sqrt(kateetti1**2 + kateetti2**2)
print ('Hypotenuusan pituus on ', hypotenuusa)


'''
helppo:
kysy ensin halutaanko hypotenuusa vai kateetti
sitten kysy joko kaksi kateettia tai kateetti ja hypotenuusa

normaali:
sama kuin helppo, mutta kysytään myös haluaako
käyttäjä tietää kolmion pinta-alan. Jos haluaa
niin lasketaan myös se ja tulostus.

vaikea:
sama kuin ed + virhekäsittelyt?





''' 