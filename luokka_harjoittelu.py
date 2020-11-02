#! /usr/bin/python3

class Ensimmainen_luokkani:
    x = 2

luokka_objekti = Ensimmainen_luokkani()
#print (luokka_objekti.x)
#print(dir(luokka_objekti))
#luokka_objekti.x = 4
#print (luokka_objekti.x)

class Robotti:
    def __init__(self, valmistaja, malli, paino, vapausasteet, tarttuja):
        self.valmistaja     = valmistaja
        self.malli          = malli
        self.paino          = paino
        self.vapausasteet   = vapausasteet
        self.tarttuja       = tarttuja
    def tulosta_ominaisuus(self, ominaisuus):
        print (ominaisuus)
        if ominaisuus == "valmistaja":
            print (self.valmistaja)
        elif ominaisuus == "malli":
            print  (self.malli)
        elif ominaisuus == "paino":
            print (self.paino)
        elif ominaisuus == "vapausasteet":
            print (self.vapausasteet)
        elif ominaisuus == "tarttuja":
            print (self.tarttuja)
        elif ominaisuus == "kaikki":
            print (self.valmistaja)
            print (self.malli)
            print (self.paino)
            print (self.vapausasteet)
            print (self.tarttuja)
        else:
            print ("ei kelvollinen ominaisuus")

if __name__ == "__main__":
    robotit = {} #=dictionary

    robotit["robotti1"] = Robotti("UniversalR", "UR3", "20", "7", "Robotiq")
    #robotit["robotti1"].tulosta_ominaisuus("kaikki")

    while True:
        action = input ("\nmita tehdaan?  ('help')  ")

        if action == "uusi":
            uusi_robotti_nimi= input("Anna uusi nimi : ")
            uusi_robotti_valmistaja = input ("Anna valmistaja : ")
            uusi_robotti_malli = input ("Anna malli : ")
            uusi_robotti_paino = input ("Anna paino : ")
            uusi_robotti_vapausasteet = input ("Anna asteet : ")
            uusi_robotti_tarttuja = input ("Anna tarttuja : ")
            robotit[uusi_robotti_nimi] = Robotti(uusi_robotti_valmistaja, 
            uusi_robotti_malli, uusi_robotti_paino,  uusi_robotti_vapausasteet, uusi_robotti_tarttuja)
        elif action == "kysy":
            print ("\nTietämäni robotit ovat: ")
            for x in robotit:
                print (" > " + x + "\n")
            kysynimi = input ("\nAnna haluamasi robotin nimi : ")
            kysyominaisuus = int(input ("1) valmistaja, 2)malli, 3)paino, 4) vapausasteet tai 5)tarttuja \n"))
            print ("Vastaus: ")
            if kysyominaisuus == 1:
                robotit[kysynimi].tulosta_ominaisuus("valmistaja")
            elif kysyominaisuus == 2:
                robotit[kysynimi].tulosta_ominaisuus("malli")
            elif kysyominaisuus == 3:
                robotit[kysynimi].tulosta_ominaisuus("paino")
            elif kysyominaisuus == 4:
                robotit[kysynimi].tulosta_ominaisuus("vapausasteet")
            elif kysyominaisuus == 5:
                robotit[kysynimi].tulosta_ominaisuus("tarttuja")
            else:
                print ("Houston we have a problem")

        elif action == "listaa":
            print ("Lista roboteista:")
            for x in robotit:
                 print (x)

        elif action == "lopeta":
            break

        elif action == "help":
            print("Käytetyt käskyt ovat: ")
            print (" uusi")
            print (" listaa")
            print (" kysy")
            print (" lopeta")
            print (" help\n")

        else:
            print ("komentoa ei löytynyt")

























