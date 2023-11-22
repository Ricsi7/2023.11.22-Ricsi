#1. Írj programot, ami kiírja a képernyőre, hogy ”Hello world!”!
szovegKiir = f"Hello Word!"
print(szovegKiir)


#2. Írj programot, beolvassa a felhasználó nevét, majd köszön neki!

# Változók
nev, szovegKiir= "", ""

nev = input("Hogy hívnak: ")

szovegKiir = f"Hello {nev}!"
print(szovegKiir)


# 3. Feladatok: Írj programot, ami beolvas egy számot, majd kiírja a kétszeresét!

# Változók
alapSzam,ketszeres, szovegKiir = 0, 0, ""

alapSzam = int(input("Kérem a számot: "))
ketszeres = 2 * alapSzam
szovegKiir = f"A szam: {alapSzam} kétszerese: {ketszeres}"

print(szovegKiir)


#4. Írj programot, ami beolvas két számot, majd kiírja:
#a. az összegüket;
#b. különbségüket;
#c. szorzatukat;
#d. hányadosukat, ha lehet!
""

# Változók
elso, masodik, osszeg, kulonbseg, szorzat, hanyados, szovegkiir = 0, 0, 0, 0, 0, 0.0

elso = int(input("Kérem az első számot: "))
masodik = int(input("Kérem a második számot: "))

osszeg = elso + masodik
kulonbseg = elso - masodik
szorzat = elso * masodik
kulonbseg = elso / masodik

szovegkiir = f"A számok: {elso}, {masodik}"
szovegkiir += f"\nösszege: {osszeg}"
szovegkiir += f"\nkülönbsége: {kulonbseg}"
szovegkiir += f"\nszorzata: {szorzat}"
szovegkiir += f"\nhányadosa: {hanyados:.4f}"

print(szovegkiir)

#5. Írj programot, mely beolvas két egész számot, és kiírja a képernyőre a nagyobbikat!

elso, masodik, harmadik, szovegKiir = 0, 0, 0,

elso = int(input("Kérem az első számot:"))
masodik = int(input("Kérem a második számot"))

if elso <= masodik:
    nagyobb = masodik
else:
    nagyobb = elso

szovegKiir = f"A nagyobb szám: {nagyobb}"

print(szovegKiir)


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