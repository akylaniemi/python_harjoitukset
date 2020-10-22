#! /usr/bin/python3
import random

#koodiin joukkoon voidaan laittaa 1-koodirivi #:lla.
''' 
useampi kommenttirivi näin
toinen rivi kommentteja
'''

muuttuja = 1
#tulostetaan
#print(muuttuja)
muuttuja = 'jiihaa'
#print (muuttuja)
muuttuja = 3
#print (muuttuja)

#print (muuttuja + 3)
#print (muuttuja)
muuttuja = muuttuja + 4
#print (muuttuja)

muuttuja = 'jotain tekstia'
#print (muuttuja)
muuttuja = muuttuja + ' vähän lisää'
#print (muuttuja)

jaettava = 3
print (type(jaettava))
jakaja = 2
print (type(jakaja))
jakojaannos = jaettava  / jakaja
print (jakojaannos)
print (type(jakojaannos))


kerrottava1 = 5
kerrottava2 = 3
tulos = kerrottava1 * kerrottava2
print (tulos)

kantaluku = 2
potenssi = 8
tulos = kantaluku**potenssi
print (tulos)

ehtomuuttuja = 'kylla1'
if ehtomuuttuja == 'kylla':
    print ('tosi')
else:
    print ('nöö')


'''
try:
    ehtonumero = int(input('Anna numero : '))

except:
    print('antamasi luku on tuhma')
    ehtonumero = float(input('Anna numero : '))

if ehtonumero > 10:
    print ('iiiso numero')
elif ehtonumero < 10:
    print ('pienempi kuin 10')
elif ehtonumero == 10:
    print ('numero on 10')


while True:
    try: 
        ehtonumero = int(inpt('Anna kokluku'))
        break

    except:
        print ('Ei kokonaisluku!')

'''
#kayttajanvastaus = int(input('Onko kaikki OK? '))
#print (kayttajanvastaus)
#print (type(kayttajanvastaus))
#AINA KAIKKI KÄYTTÄJÄLTÄ TULEVA ON STR

nimilista1 = ['sari', 'miia', 'kaija']
nimilista2 = ['eki', 'jussi', 'niilo']
print (nimilista1)
print (nimilista1[1]) #alkaa nollasta...
nimilista = nimilista1 + nimilista2
print (nimilista)

#print (nimilista[random.randrange(6)])

print (nimilista[random.randrange(len(nimilista))])























