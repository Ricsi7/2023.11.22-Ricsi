#6. Írj programot, mely beolvas három egész számot, és kiírja a képernyőre a legkisebbet!

# Változók
elso, masodik, harmadik, legkisebb, SzovegKiir = 0, 0, 0, 0 ""

# Segédváltozók
kisebb = 0

elso = int(input("Kérem az első számot: "))
masodik = int(input("Kérem a második számot: "))
harmadik = int(input("Kérem a harmadik számot: "))

if elso <= masodik:
    kisebb = elso
else:
    kisebb = masodik

if kisebb <= harmadik:
    legkisebb = kisebb
else:
    legkisebb = harmadik

SzovegKiir = f"A legkisebb szám: {legkisebb}"
print(SzovegKiir)