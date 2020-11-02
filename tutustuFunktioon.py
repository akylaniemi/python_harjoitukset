#! /usr/bin/python3
import random

def funktio_palautuksella(input1, input2, input3):
    output  = input1 + input2 + input3
    
    return output


    ###################################################

#loput ajetaan vain jos tämä on päajotiedosto:
if __name__ == "_main_":

    vastaus = funktio_palautuksella(1, 4,5)
    print (vastaus)

    vastaus = funktio_palautuksella(1, 2, 3)
    print (vastaus)
    '''
    #tuntitehtava: muokkaa funtiota niin että se ottaa
    #sisään 3 argumenttia.
    # funktion kutsussa on luvut 1,4,5

    osa2: tee uusi muuttujaoutput2 ja tallenna siihen
    muuttujaan 1,2,3
    '''
    for x in range(10):
        vastaus2 = funktio_palautuksella(x, random.randrange(30), 8)
        print (x, vastaus2)

    luku1_in = int(input("anna luku : "))
    luku2_in = int(input("anna luku : "))
    luku3_in = int(input("anna luku : "))

    vastaus3 = funktio_palautuksella(luku1_in, luku2_in, luku3_in)
    print (vastaus3)