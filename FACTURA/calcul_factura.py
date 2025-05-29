import pygame


dict_produse = { }
with open('produse.txt', 'r') as f:
    next(f) #trecem peste prima linie din fiisier
    for p in f:
        comp = p.strip().split(', ')
        dict_produse[comp[0]] = float(comp[1])

linii_cumparaturi = []
with open('cumparaturi.txt', 'r') as g:
    next(g) #trece peste prima linie din fisier
    for c in g:
        comp2 = c.strip().split(', ')
        linii_cumparaturi.append(comp2)

Pret_total = 0
with open('factura.txt', 'w') as h:
    for lc in linii_cumparaturi:
        nume_produs = lc[0]
        cantitate = float(lc[1])
        pret = dict_produse[nume_produs]
        Pret_total += pret*cantitate 
    h.write(f"Pret total : {Pret_total}")



    