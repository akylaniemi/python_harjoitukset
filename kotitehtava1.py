#! /usr/bin/python3

import sys
from math import sqrt


print (' ')
print ('      Tehtava 1 - hypotenuusan ja/tai kateetin laskenta')
print ('--------------------------- + kolmion pinta-ala ---------------')
print ('--- (Pituuksia antaessasi kayta pistetta desimaalipilkkuna) ---')
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
    kateetti1 = float(input('Anna 1. sivu           :  '))
    kateetti2 = float(input('Anna 2. sivu           :  '))
    hypotenuusa  = sqrt(kateetti1**2 + kateetti2**2)
    hypotenuusa2 = round(hypotenuusa, 2)
    print ('Hypotenuusan pituus on : ', hypotenuusa2)
    #Lasketaan käyttäjän halutessa myös pinta-ala:
    if valinta == 3:
        pinta  = (kateetti1 * kateetti2) / 2
        pinta2 = round(pinta, 2)
        print ('Pinta-ala on           : ', pinta2)

#Kateetti ja pinta-ala
elif valinta == 2 or valinta == 4:
    hypotenuusa = float(input('Anna Hypotenuusa          :  '))
    kateetti1   = float(input('Anna sivun pituus         :  '))
    if hypotenuusa > kateetti1:
        kateetti2  = sqrt(hypotenuusa**2 - kateetti1**2)
        kateetti22 = round(kateetti2, 2)
        print ('Puuttuvan sivun pituus on : ', kateetti22)
        
        #Lasketaan käyttäjän halutessa myös pinta-ala
        if valinta == 4:
            pinta  = (kateetti1 * kateetti2) / 2
            pinta2 = round(pinta, 2)
            print ('Pinta-ala on              : ', pinta2)

    else:
        print (' ')
        print ('Hypotenuusan olisi hyva olla pidempi kuin kateetti...')
    
        
#Virhekäsittely, poistutaan phjelmasta.
else:
    print (' ')
    sys.exit('Valintasi oli hyvä mutta väärin. Koeta uudelleen...')


print (' ')
