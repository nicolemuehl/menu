# -*- coding: utf-8 -*-

print "Hallo, wie lautet dein heutiges Tagesmenü?"

ts = raw_input("Tagessuppe: ")
tsp = raw_input("Preis: ")

tg = raw_input("Hauptspeise: ")
tgp = raw_input("Preis: ")

td = raw_input("Dessert: ")
tdp = raw_input("Preis: ")

a = "***Tagessuppe***\n%s: € %s\n\n" %(ts, tsp)
b = "***Hauptspeise***\n%s: € %s\n\n" %(tg, tgp)
c = "***Dessert***\n%s: € %s\n\n" %(td, tdp)

print a+b+c

with open("menu.txt", "w+") as (speisekarte):
    speisekarte.write("Tagesmenü\n\n")
    speisekarte.write(a+b+c)