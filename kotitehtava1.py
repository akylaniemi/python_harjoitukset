#! /usr/bin/python3

import sys
from math import sqrt


print (' ')
print ('Tehtava 1 - hypotenuusan ja/tai kateetin laskenta')
print ('------------- + kolmion pinta-ala ---------------')
print (' ')

#Kysytään käyttäjän valitsema toiminne
print ('Lasketaanko:')
print ('1. Hypotenuusa,')
print ('2. Kateetti,')
print ('3. Hypotenuusa ja pinta-ala, vai')

#Luetaan kokonaisluku ja suodatetaan muut syötteet pois:
try:
    valinta = int(input ('4. Kateetti ja pinta-ala?        '))
except:
    print (' ')
    sys.exit('Antamasi valinta ei ollut kokonaisluku.')

print (' ')

#Käsitellään käyttäjän valinta virhekäsittelyineen:
#Hypotenuusa ja pinta-ala
if valinta == 1 or valinta == 3:
    kateetti1 = int(input('Anna 1. sivu           :  '))
    kateetti2 = int(input('Anna 2. sivu           :  '))
    hypotenuusa = sqrt(kateetti1**2 + kateetti2**2)
    print ('Hypotenuusan pituus on : ', hypotenuusa)
    #Lasketaan käyttäjän halutessa myös pinta-ala:
    if valinta == 3:
        pinta = (kateetti1 * kateetti2) / 2
        print ('Pinta-ala on           : ', pinta)

#Kateetti ja pinta-ala
elif valinta == 2 or valinta == 4:
    hypotenuusa = int(input('Anna Hypotenuusa          :  '))
    kateetti1   = int(input('Anna sivun pituus         :  '))
    kateetti2 = sqrt(hypotenuusa**2 - kateetti1**2)
    print ('Puuttuvan sivun pituus on : ', kateetti2)
    #Lasketaan käyttäjän halutessa myös pinta-ala hieman suoremmin:
    if valinta == 4:
        print ('Pinta-ala on              : ', (kateetti1 * kateetti2) / 2) 

#Virhekäsittely, poistutaan phjelmasta.
else:
    print (' ')
    sys.exit('Valintasi oli hyvä mutta väärin. Koeta uudelleen...')


print (' ')
