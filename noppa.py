#! /usr/bin/python3

import random
import sys

__name__ = '_main_'

def fNoppa(noppalkm, taholkm):

    noppasumma = 0

    if noppalkm == 0:
        try:
            noppalkm = int(input("Montako noppaa haluat käyttää (kokonaisluku)?: "))
        except:
            sys.exit("Antamasi vastaus ei ollut kokonaisluku.")

    if taholkm == 0:
        try:
            taholkm = int(input("Monitahoista noppaa haluat käyttää (kokonaisluku)?: "))
        except:
            sys.exit("Antamasi vastaus ei ollut kokonaisluku.")
    
    noppa_tahokas = [i for i in range(1, taholkm + 1)]
    print ("\nSilmälukulista: ", (noppa_tahokas))

    for x in range(noppalkm):
        print ("\nNoppa nro_", x+1)
        #satunnainen = random.randrange(taholkm+1)                      #got zero as an answer, not good, so ->
        satunnainen = random.randint(1, taholkm+1)
        print ("Satunnainen noppatulos: ", satunnainen)
        noppasumma = noppasumma + satunnainen

    print ("\nSatunnaiset noppatulokset summattuna: ", noppasumma) 

    return (noppalkm, taholkm)



###################################################################################################

#loput ajetaan vain jos tämä on päajotiedosto:
if __name__ == "_main_":

    print ("\n*** N O P P A - h a r j o i t u s ***")
    print ("-------------------------------------")

    (maara, tahot) = fNoppa (0,0)

    while True:
        try:
            print ("\n- - Halutaanko heittää uudelleen? - -")
            print ("  ENTER       = uusi heittokierros, ")
            print ("  muuta tahot = uusi taholukumäärä, ")
            print ("  muuta lkm   = uusi noppalkm?      ")
            jatko = input("  lopeta      = ohjelman lopetus?     >")
        except:
            sys.exit("yritäppä uudelleen")


        if jatko.upper() == "ENTER" or jatko == "":
            fNoppa (maara, tahot)
        elif jatko == "muuta tahot":
                (maara, tahot) = fNoppa(maara, 0)
        elif jatko == "muuta lkm":
                (maara, tahot) = fNoppa(0, tahot)
        elif jatko == "lopeta":
            sys.exit("\nHave a nice day!\n")


#Tämä oli hyvä harjoitus, paransi Python-näppituntumaa funktioiden suhteen mukavasti.
#...ja tää tuntui aika kivalta=tiiviiltä ratkaisulta.

#helppo

#Kysy kauttajalta kuinka monta tahoista noppaa kayttaja haluaa heittaa.                             OK
#Tee funtio joka ottaa sisaansa tahojen lukumaaran ja palauttaa listan jossa on nopan silmaluvut.   OK
#Anna satunnainen nopantulos printtaamalla se kayttajalle.                                          OK

#normaali

#sama kuin normaali, mutta kysy kuinka monta noppaa kayttaja haluaa heittaa, ja printtaa            OK
# noppien tulos erikseen ja summana                                                                 OK, OK


#vaikea

#Sama kuin normaali, mutta tuloksen jalkeen kysy kayttajalta halutaanko heittaa uudelleen.          OK
#entterilla uusi heitto                                                                             OK
#muuta noppa kysyy uudelleen tahot                                                                  OK ('muuta tahot')
#muuta noppien lukumaara kysyy noppaluvun uudelleen                                                 OK ('muuta lkm')
#lopeta lopettaa ohjelman                                                                           OK