#! /usr/bin/python3

import time

luku1 = 1
print (" ")
luku2 = 1
print (luku1)
print ("")
print (luku2)
laskuri = 0

#while laskuri != 10:
while True:
    valiluku = luku2
    luku2 = luku1 + luku2
    luku1 = valiluku
    print ("")
    print (luku2)
    laskuri = laskuri + 1
    time.sleep(0.4)
    if laskuri > 10:
        break

